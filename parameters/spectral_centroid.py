import numpy as np
import matplotlib.pyplot as plt


def spectral_centroid(magnitudes, freq_bin):
    """
    :param magnitudes: array, complex values of each freqnecy bin
    :param freq_bin: array, freqnecy bins

    :returns: sc_left - array, spectral centroid of left channel for each window
              sc_right - array, spectral centroid of right channel for each window
                         if file is mono returns -1
    """
    # puste macierze na parametry dla kazdego okna
    sc_left = np.array([])
    sc_right = np.array([])

    shape = len(magnitudes.shape)

    # obsluga plików mono
    if shape == 2:
        # iteracja po okienkach
        for window in magnitudes.T:
            # algorytm spectral centroid, jest to właściwie średnia ważona danych częstotliwości występujących w widmie
            # razy ich amplituda podzielić na te częstotliwości
            sc = np.sum(np.abs(window) * freq_bin) / np.sum(np.abs(window))
            # przypisanie do macierzy zwrotnej
            sc_left = np.append(sc_left, sc)
        # dla plików mono kanał prawy zwraca "-1"
        sc_right = -1

    # obsługa plików dwukanałowych
    elif shape == 3:
        for window in magnitudes[0].T:
            sc = np.sum(np.abs(window) * freq_bin) / np.sum(np.abs(window))
            sc_left = np.append(sc_left, sc)

        for window in magnitudes[1].T:
            sc = np.sum(np.abs(window) * freq_bin) / np.sum(np.abs(window))
            sc_right = np.append(sc_right, sc)

    # jeśli coś nie zgadza się z rozimiarem macierzy wejściowej to robimy error, oczywiście nie przewiduje to wszystkich
    # przypadków, na przykład gdy :magnitudes: ma odpowiedni "kształt" ale złe wartości
    else:
        raise ValueError("Input is not supported")

    return sc_left, sc_right


def spectral_centroid_debug(sc_left, sc_right, time_bin, duration, sampling_rate, data):
    """
    :param sc_left: array, spectral centroids of left channel or mono file
    :param sc_right: array or int, spectral centroids of right channel or -1 if file is mono
    :param time_bin: array, time bins
    :param duration: float,  duration of the wav file
    :param sampling_rate: float, sampling rate of the wav file
    :param data: array, wav file values
    """

    time = np.linspace(0, duration, duration * sampling_rate)

    fig = plt.figure(1)
    fig.canvas.set_window_title('Spectral Centroid')

    if type(sc_right) != type(sc_left):
        plot, plot_mono = plt.subplots()
        plot_mono.plot(time_bin, sc_left, color='#23108f', linewidth=0.8, label="Spectral Centroid")
        plot_mono.set_xlabel('Time [s]')
        plot_mono.set_ylabel('Centroid [Hz]')
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
        plot_l = plt.subplot2grid((2, 2), (0, 0))
        plot_r = plt.subplot2grid((2, 2), (0, 1))
        plot_both = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l.plot(time_bin, sc_left, color='#23108f', linewidth=0.8, label='Spectral Centroid')
        plot_l.set_title('Left channel')
        plot_l.set_xlabel('Time [s]')
        plot_l.set_ylabel('Centroid [Hz]')
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

        plot_r.plot(time_bin, sc_right, color='r', linewidth=0.8, label='Spectral Centroid')
        plot_r.set_title('Right channel')
        plot_r.set_xlabel('Time [s]')
        plot_r.set_ylabel('Centroid [Hz]')
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

        plot_both.plot(time_bin, sc_left, color='#23108f', linewidth=0.8, zorder=10, label='Left')
        plot_both.plot(time_bin, sc_right, color='#de0000', linewidth=0.8, zorder=11, label='Right')
        plot_both.set_title('Both channels')
        plot_both.set_xlabel('Time [s]')
        plot_both.set_ylabel('Centroid [Hz]')
        plot_both.minorticks_on()
        plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_both.set_xlim(left=-1, right=time_bin[-1] + 1)
        plot_both.legend(loc='upper left')

        plt.subplots_adjust(wspace=0.25)
    plt.suptitle('Spectral Centroid', fontsize=16)


