import numpy as np


def spectral_centroid(magnitudes, freq_bin):
    """
    :param magnitudes: array, complex values of each freqnecy bin
    :param freq_bin: array, freqnecy bin
    :returns: sc_left - array, spectral centroid of left channel for each window
              sc_right - array, spectral centroid of right channel for each window
                         if file is mono returns -1
    """
    # puste macierze na parametry dla kazdego okna
    sc_left = np.array([])
    sc_right = np.array([])

    # obsluga plików mono
    if len(magnitudes.shape) == 2:
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
    elif len(magnitudes.shape) == 3:
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
