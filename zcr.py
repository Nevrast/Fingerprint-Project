import numpy as np


def zero_crossing(ch_left, ch_right=None):

    zcr_left = np.array([])
    zcr_right = np.array([])

    for i in ch_left:
        zc = 0

        for j in range(int(i.shape[0])-1):
            if i[j] == 0:
                i[j] = -1
            if i[j] > 0 and i[j+1] < 0:
                zc += 1
            elif i[j] < 0 and i[j+1] > 0:
                zc += 1

        zcr_left = np.append(zcr_left, zc)

    if type(ch_right) == type(ch_left):
        for i in ch_right:
            zc = 0

            for j in range(int(i.shape[0])-1):
                if i[j] == 0:
                    i[j] = -1
                if i[j] > 0 and i[j+1] < 0:
                    zc += 1
                elif i[j] < 0 and i[j+1] > 0:
                    zc += 1

            zcr_right = np.append(zcr_right, zc)
    else:
        zcr_right = -1
    return np.sum(zcr_left), np.sum(zcr_right)



