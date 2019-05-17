import numpy as np
import matplotlib.pyplot as plt


def rms(left_channel, right_channel):
    """
    :param left_channel: array2D, windowed left channel
    :param right_channel: array2D, windowed right channel, non if signal is mono
    :return: rms_left: array, rms for each window in left channel
             rms_right: array, rms for each window in left channel
    """

    # puste macierze do przypisania wartosci skutecznej rms
    rms_left = np.array([])
    rms_right = np.array([])

    #iteracja po lewym kanale
    for i in left_channel:
        rms = np.sqrt(np.sum(np.power(i, 2)/len(i)))
        rms_left = np.append(rms_left, rms)

    if type(right_channel) == type(left_channel):
        for i in right_channel:
            rms = np.sqrt(np.sum(np.power(i, 2) / len(i)))
            rms_right = np.append(rms_right, rms)

    else:
        rms_right = -1

    return rms_left, rms_right


def rms_debug(rms_left, rms_right, time_bin, duration, sampling_rate, data):
    time = np.linspace(0, duration, duration * sampling_rate)

    fig = plt.figure(4)
    fig.canvas.set_window_title('Root Mean Square')

    if type(rms_right) != type(rms_left):
        plot_mono = plt.subplot2grid((1, 1), (0, 0))
        plot_mono.plot(time_bin, rms_left, color='#23108f', linewidth=0.8, label='Root Mean Square')
        plot_mono.set_xlabel('Time [s]')
        plot_mono.set_ylabel('Centroid [Hz]')
        plot_mono.minorticks_on()
        plot_mono.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_mono.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_mono.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_signal_mono = plot_mono.twinx()
        plot_signal_mono.plot(time, data, color='#c6c6c6', linewidth=0.4, label='Signal')
        plot_signal_mono.set_ylabel('Normalized amplitude')
        plot_mono.set_zorder(plot_signal_mono.get_zorder() + 1)
        plot_mono.patch.set_visible(False)
        plot_mono.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_mono.legend(loc='lower right', bbox_to_anchor=(1., 1.))

    else:
        plot_l = plt.subplot2grid((2, 2), (0, 0))
        plot_r = plt.subplot2grid((2, 2), (0, 1))
        plot_both = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l.plot(time_bin, rms_left, color='#23108f', linewidth=0.8, label='Root Mean Square')
        plot_l.set_title('Left channel')
        plot_l.set_xlabel('Time [s]')
        plot_l.set_ylabel('Zero Crossing')
        plot_l.minorticks_on()
        plot_l.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_l.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_l.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_signal_l = plot_l.twinx()
        plot_signal_l.plot(time, data[0].flat, color='#c6c6c6', linewidth=0.4, label='Signal')
        plot_signal_l.set_ylabel('Normalized amplitude')
        plot_l.set_zorder(plot_signal_l.get_zorder() + 1)
        plot_l.patch.set_visible(False)
        plot_l.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_l.legend(loc='lower right', bbox_to_anchor=(1., 1.))

        plot_r.plot(time_bin, rms_right, color='r', linewidth=0.8, label='Root Mean Square')
        plot_r.set_title('Right channel')
        plot_r.set_xlabel('Time [s]')
        plot_r.set_ylabel('Root Mean Square')
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

        plot_both.plot(time_bin, rms_left, color='#23108f', linewidth=0.8, zorder=10, label='Left')
        plot_both.plot(time_bin, rms_right, color='#de0000', linewidth=0.8, zorder=11, label='Right')
        plot_both.set_title('Both channels')
        plot_both.set_xlabel('Time [s]')
        plot_both.set_ylabel('Root Mean Square')
        plot_both.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_both.minorticks_on()
        plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_both.legend(loc='upper left')

        plt.subplots_adjust(wspace=0.25)
    plt.suptitle('Root Mean Square', fontsize=16)

