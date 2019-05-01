import numpy as np


def spectral_centroid(magnitudes, freq_bin):
    """
    :param magnitudes: array, complex values of each freqnecy bin
    :param freq_bin: array, freqnecy bin
    :returns: sc_left - array, spectral centroid of left channel for each window
              sc_right - array, spectral centroid of right channel for each window
                         if file is mono returns -1
    """

    sc_left = np.array([])
    sc_right = np.array([])
    if len(magnitudes.shape) == 2:
        for window in magnitudes.T:
            sc = np.sum(np.abs(window)*freq_bin) / np.sum(np.abs(window))
            sc_left = np.append(sc_left, sc)
        sc_right = -1

    elif len(magnitudes.shape) == 3:
        for window in magnitudes[0].T:
            sc = np.sum(np.abs(window)*freq_bin) / np.sum(np.abs(window))
            sc_left = np.append(sc_left, sc)
        for window in magnitudes[1].T:
            sc = np.sum(np.abs(window)*freq_bin) / np.sum(np.abs(window))
            sc_right = np.append(sc_right, sc)
    else:
        raise ValueError("Input is not supported")

    return sc_left, sc_right
