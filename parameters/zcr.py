import numpy as np


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
