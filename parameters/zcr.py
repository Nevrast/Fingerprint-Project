import numpy as np
import matplotlib.pyplot as plt


def zero_crossing(ch_left, ch_right=None):
    r"""
    :param ch_left: array2D, windowed left channel
    :param ch_right: array2D, windowed right channel, None if signal is mono
    :return: zc_left: array, zero crossing for each window in left channel,
    zc_right: array, zero crossing for each window in right channel
    """

    # puste macierze do przypisania przejść przez zero
    zc_left = np.array([])
    zc_right = np.array([])

    # iteracja po oknach kanału lewego
    for i in ch_left:
        # zmienna przechowująca ilość przejść przez zero
        zc = 0
        # iteracja po kolejnych elementach okienka, bez ostatniego elementu
        for j in range(int(i.shape[0]) - 1):
            # jeśli znak i-tego elementu nie równa się znakowi i+1 elementu to nastąpiło przejście przez zero
            if sign(i[j]) != sign(i[j + 1]):
                zc += 1
        # przypisanie do macierzy do zwrotu
        zc_left = np.append(zc_left, zc)

    # sprawdzanie czy kanał prawy został podany
    if type(ch_right) == type(ch_left):
        for i in ch_right:
            zc = 0
            for j in range(int(i.shape[0])-1):
                if sign(i[j]) != sign(i[j + 1]):
                    zc += 1
            zc_right = np.append(zc_right, zc)
    else:
        zc_right = -1
    return zc_left, zc_right


def sign(value):
    if value <= 0:
        return False
    elif value > 0:
        return True


def zero_crossing_debug(zc_left, zc_right, time_bin, duration, sampling_rate, data):
    time = np.linspace(0, duration, duration * sampling_rate)

    fig = plt.figure(3)
    fig.canvas.set_window_title('Zero Crossing')

    if type(zc_right) != type(zc_left):
        plot_mono = plt.subplot2grid((1, 1), (0, 0))
        plot_mono.plot(time_bin, zc_left, color='#23108f', linewidth=0.8, label="Spectral Centroid")
        plot_mono.set_xlabel('Time [s]')
        plot_mono.set_ylabel('Centroid [Hz]')
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

        plot_l.plot(time_bin, zc_left, color='#23108f', linewidth=0.8, label='Zero Crossing')
        plot_l.set_title('Left channel')
        plot_l.set_xlabel('Time [s]')
        plot_l.set_ylabel('Zero Crossing')
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

        plot_r.plot(time_bin, zc_right, color='r', linewidth=0.8, label='Zero Crossing')
        plot_r.set_title('Right channel')
        plot_r.set_xlabel('Time [s]')
        plot_r.set_ylabel('Zero Crossing')
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

        plot_both.plot(time_bin, zc_left, color='#23108f', linewidth=0.8, zorder=10, label='Left')
        plot_both.plot(time_bin, zc_right, color='#de0000', linewidth=0.8, zorder=11, label='Right')
        plot_both.set_title('Both channels')
        plot_both.set_xlabel('Time [s]')
        plot_both.set_ylabel('Zero Crossing')
        plot_both.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_both.minorticks_on()
        plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_both.legend(loc='upper left')

        plt.subplots_adjust(wspace=0.25)
    plt.suptitle('Zero Crossing', fontsize=16)
