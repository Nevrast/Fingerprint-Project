import numpy as np
"""
input: magnicute of the STFT
output: spectral_roll_off
"""

def roll_off(magnitudes):
    ro_left = np.array([])
    ro_right = np.array([])

    if len(magnitudes.shape) == 2: #obliczenia dla dźwięku mono
        for window in magnitudes.T:
            ro = 0.85 * np.sum(np.abs(window)) #obliczenie roll off
            ro_left = np.append(ro_left, ro)

        ro_right = -1

    elif len(magnitudes.shape) == 3: #obliczenia dla dźwięku stereo
        for window in magnitudes[0].T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_left = np.append(ro_left, ro)

        for window in magnitudes[1].T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_right = np.append(ro_right, ro)

    else:
        raise ValueError("Input is not supported")

    return ro_left, ro_right