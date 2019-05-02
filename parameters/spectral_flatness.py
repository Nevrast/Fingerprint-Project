import numpy as np


def spectral_flatness(magnitudes):
    """
    :param magnitudes: array, complex values of each freqnecy bin
    :returns: sc_left - array, spectral flatness of left channel for each window
              sc_right - array, spectral flatness of right channel for each window
                         if file is mono returns -1
    """
    # puste macierze na parametry dla kazdego okna
    sf_left = np.array([])
    sf_right = np.array([])

    # obsluga plików mono
    if len(magnitudes.shape) == 2:
        # długość okna
        N = magnitudes.shape[0]

        # iteracja po okienkach
        for window in magnitudes.T:
            # algorytm spectral flatness, czyli średnia geometryczna podzielić na średnia arytmetyczna
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            # przypisanie do macierzy zwrotnej
            sf_left = np.append(sf_left, flatness)
        # dla plików mono kanał prawy zwraca "-1"
        sf_right = -1

    # obsługa plików dwukanałowych
    elif len(magnitudes.shape) == 3:
        N = magnitudes.shape[1]

        for window in magnitudes[0].T:
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            sf_left = np.append(sf_left, flatness)

        for window in magnitudes[1].T:
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            sf_right = np.append(sf_right, flatness)

    # jeśli coś nie zgadza się z rozimiarem macierzy wejściowej to robimy error, oczywiście nie przewiduje to wszystkich
    # przypadków, na przykład gdy :magnitudes: ma odpowiedni "kształt" ale złe wartości
    else:
        raise ValueError("Input is not supported")

    return sf_left, sf_right

