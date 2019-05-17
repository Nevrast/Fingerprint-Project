import numpy as np

def rms(left_channel, right_channel):


    # puste macierze do przypisania wartosci skutecznej rms
    rms_left = np.array([])
    rms_right = np.array([])

    #iteracja po lewym kanale
    for i in left_channel:
        squares = np.power(i, 2)
        rms_left = squares
    rms_right = -1

    return rms_left, rms_right


