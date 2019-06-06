import numpy as np
import scipy.signal as sl
import matplotlib.pyplot as plt


def wrapper(windows, sampling_rate, window_shape):
    freqs, psd = sl.periodogram(windows, fs=sampling_rate, window=window_shape)
    return psd


def power_spectral_density(psd_left, psd_right, sampling_rate, window):
    av_psd_l = np.array([])
    av_psd_r = np.array([])
    psd_l = wrapper(psd_left, sampling_rate, window)
    for i in psd_l:
        av_psd_l = np.append(av_psd_l, np.average(i))
    if type(psd_right) != type(psd_left):
        av_psd_r = -1
    else:
        psd_r = wrapper(psd_right, sampling_rate, window)

        for i in psd_r:
            av_psd_r = np.append(av_psd_r, np.average(i))
    return av_psd_l, av_psd_r


def power_spectral_density_debug(psd_left, psd_right, time_bin, duration, sampling_rate, data):
    """
    :param psd_left: array, average power spectral density of left channel or mono file
    :param psd_right: array or int, average power spectral density or -1 if file is mono
    :param time_bin: array, time bins
    :param duration: float,  duration of the wav file
    :param sampling_rate: float, sampling rate of the wav file
    :param data: array, wav file values
    """

    time = np.linspace(0, int(duration), int(duration * sampling_rate))

    fig = plt.figure(6)
    fig.canvas.set_window_title('Average power spectral density')

    if type(psd_right) != type(psd_left):
        plot_mono = plt.subplot2grid((1, 1), (0, 0))
        plot_mono.plot(time_bin, psd_left, color='#23108f', linewidth=0.8, label="Average PSD")
        plot_mono.set_xlabel('Time [s]')
        plot_mono.set_ylabel('Average PSD')
        plot_mono.minorticks_on()
        plot_mono.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_mono.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_mono.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_signal_mono = plot_mono.twinx()
        plot_signal_mono.plot(time, data.flat, color='#c6c6c6', linewidth=0.4, label="Signal")
        plot_signal_mono.set_ylabel('Normalized amplitude')
        plot_mono.set_zorder(plot_signal_mono.get_zorder() + 1)
        plot_mono.patch.set_visible(False)
        plot_mono.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_mono.legend(loc='lower right', bbox_to_anchor=(1., 1.))

    else:
        plt.tight_layout(pad=1.0, w_pad=0.5)
        plot_l = plt.subplot2grid((2, 2), (0, 0))
        plot_r = plt.subplot2grid((2, 2), (0, 1))
        plot_both = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l.plot(time_bin, psd_left, color='#23108f', linewidth=0.8, label='Average PSD')
        plot_l.set_title('Left channel')
        plot_l.set_xlabel('Time [s]')
        plot_l.set_ylabel('Average PSD')
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

        plot_r.plot(time_bin, psd_right, color='r', linewidth=0.8, label='Average PSD')
        plot_r.set_title('Right channel')
        plot_r.set_xlabel('Time [s]')
        plot_r.set_ylabel('Average PSD')
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

        plot_both.plot(time_bin, psd_left, color='#23108f', linewidth=0.8, zorder=10, label='Left')
        plot_both.plot(time_bin, psd_right, color='#de0000', linewidth=0.8, zorder=11, label='Right')
        plot_both.set_title('Both channels')
        plot_both.set_xlabel('Time [s]')
        plot_both.set_ylabel('Average PSD')
        plot_both.minorticks_on()
        plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_both.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_both.legend(loc='upper left')

        plt.subplots_adjust(wspace=0.25)
    plt.suptitle('Average Power Spectral Density', fontsize=16)
