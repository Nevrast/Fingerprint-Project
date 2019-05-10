import numpy as np


def roll_off(magnitudes):
    ro_left = np.array([])
    ro_right = np.array([])

    if len(magnitudes.shape) == 2:
        for window in magnitudes.T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_left = np.append(ro_left, ro)

        ro_right = -1

    elif len(magnitudes.shape) == 3:
        for window in magnitudes[0].T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_left = np.append(ro_left, ro)

        for window in magnitudes[1].T:
            ro = 0.85 * np.sum(np.abs(window))
            ro_right = np.append(ro_right, ro)

    else:
        raise ValueError("Input is not supported")

    return ro_left, ro_right
