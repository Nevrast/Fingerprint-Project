import numpy as np
import matplotlib.pyplot as plt


def roll_off(magnitudes):
    """
    input: magnicute of the STFT
    output: spectral_roll_off
    """
    ro_left = np.array([])
    ro_right = np.array([])

    if len(magnitudes.shape) == 2:  # obliczenia dla dźwięku mono
        for window in magnitudes.T:
            ro = 0.85 * np.sum(np.abs(window))  # obliczenie roll off
            ro_left = np.append(ro_left, ro)

        ro_right = -1

    elif len(magnitudes.shape) == 3:  # obliczenia dla dźwięku stereo
        for window in magnitudes[0].T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_left = np.append(ro_left, ro)

        for window in magnitudes[1].T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_right = np.append(ro_right, ro)

    else:
        raise ValueError("Input is not supported")

    return ro_left, ro_right


def roll_off_debug(ro_left, ro_right, time_bin, duration, sampling_rate, data):

    time = np.linspace(0, duration, duration * sampling_rate)

    fig = plt.figure(5)
    fig.canvas.set_window_title('Spectral Roll Off')

    if type(ro_right) != type(ro_left):
        plot_mono = plt.subplot2grid((1, 1), (0, 0))
        plot_mono.plot(time_bin, ro_left, color='#23108f', linewidth=0.8, label="Spectral Roll Off")
        plot_mono.set_xlabel('Time [s]')
        plot_mono.set_ylabel('Spectral Roll Off')
        plot_mono.minorticks_on()
        plot_mono.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_mono.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_mono.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_signal_mono = plot_mono.twinx()
        plot_signal_mono.plot(time, data, color='#c6c6c6', linewidth=0.4, label="Signal")
        plot_signal_mono.set_ylabel('Normalized amplitude')
        plot_mono.set_zorder(plot_signal_mono.get_zorder() + 1)
        plot_mono.patch.set_visible(False)
        plot_mono.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_mono.legend(loc='lower right', bbox_to_anchor=(1., 1.))

    else:
        plot_l = plt.subplot2grid((2, 2), (0, 0))
        plot_r = plt.subplot2grid((2, 2), (0, 1))
        plot_both = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l.plot(time_bin, ro_left, color='#23108f', linewidth=0.8, label='Spectral Roll Off')
        plot_l.set_title('Left channel')
        plot_l.set_xlabel('Time [s]')
        plot_l.set_ylabel('Spectral Roll Off')
        plot_l.minorticks_on()
        plot_l.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_l.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_l.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_signal_l = plot_l.twinx()
        plot_signal_l.plot(time, data[0].flat, color='#c6c6c6', linewidth=0.4, label="Signal")
        plot_signal_l.set_ylabel('Normalized amplitude')
        plot_l.set_zorder(plot_signal_l.get_zorder() + 1)
        plot_l.patch.set_visible(False)
        plot_l.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_l.legend(loc='lower right', bbox_to_anchor=(1., 1.))

        plot_r.plot(time_bin, ro_right, color='r', linewidth=0.8, label='Spectral Roll Off')
        plot_r.set_title('Right channel')
        plot_r.set_xlabel('Time [s]')
        plot_r.set_ylabel('Spectral Roll Off')
        plot_r.minorticks_on()
        plot_r.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_r.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
        plot_r.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_signal_r = plot_r.twinx()
        plot_signal_r.plot(time, data[1].flat, color='#c6c6c6', linewidth=0.4, label='Signal')
        plot_signal_r.set_ylabel('Normalized amplitude')
        plot_r.set_zorder(plot_signal_r.get_zorder() + 1)
        plot_r.patch.set_visible(False)
        plot_r.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_r.legend(loc='lower right', bbox_to_anchor=(1., 1.))

        plot_both.plot(time_bin, ro_left, color='#23108f', linewidth=0.8, zorder=10, label='Left')
        plot_both.plot(time_bin, ro_right, color='#de0000', linewidth=0.8, zorder=11, label='Right')
        plot_both.set_title('Both channels')
        plot_both.set_xlabel('Time [s]')
        plot_both.set_ylabel('Spectral Roll Off')
        plot_both.minorticks_on()
        plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_both.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_both.legend(loc='upper left')

        plt.subplots_adjust(wspace=0.25)
    plt.suptitle('Spectral Roll Off', fontsize=16)
