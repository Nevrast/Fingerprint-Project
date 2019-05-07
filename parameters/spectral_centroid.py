import numpy as np
import matplotlib.pyplot as plt

def spectral_centroid(magnitudes, freq_bin, time_bin, debug=False):
    """
    :param magnitudes: array, complex values of each freqnecy bin
    :param freq_bin: array, freqnecy bins
    :param time_bin: array, time bins
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
    if debug:
        if shape == 2:
            plt.plot(time_bin, sc_left, color='b', linewidth=0.8)
            plt.title('Left channel')
            plt.xlabel('Time [s]')
            plt.ylabel('Centroid [Hz]')
            plt.minorticks_on()
            plt.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
            plt.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)

        if shape == 3:
            plot_l = plt.subplot2grid((2, 2), (0, 0))
            plot_r = plt.subplot2grid((2, 2), (0, 1))
            plot_both = plt.subplot2grid((2, 2), (1, 0), colspan=2)

            plot_l.plot(time_bin, sc_left, color='b', linewidth=0.8)
            plot_l.set_title('Left channel')
            plot_l.set_xlabel('Time [s]')
            plot_l.set_ylabel('Centroid [Hz]')
            plot_l.minorticks_on()
            plot_l.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
            plot_l.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)

            plot_r.plot(time_bin, sc_right, color='r', linewidth=0.8)
            plot_r.set_title('Right channel')
            plot_r.set_xlabel('Time [s]')
            plot_r.set_ylabel('Centroid [Hz]')
            plot_r.minorticks_on()
            plot_r.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
            plot_r.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)

            plot_both.plot(time_bin, sc_left, color='b', linewidth=0.8)
            plot_both.plot(time_bin, sc_right, color='r', linewidth=0.8)
            plot_both.set_title('Both channels')
            plot_both.set_xlabel('Time [s]')
            plot_both.set_ylabel('Centroid [Hz]')
            plot_both.minorticks_on()
            plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
            plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)

        plt.show()
    return sc_left, sc_right
