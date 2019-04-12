from wave_to_array import wave_to_array
from sine_gen import sine_generator
import matplotlib.pyplot as plt
import numpy as np

sine_generator(10.0, 1.0, 50, True)
sr, left, right = wave_to_array('yamaha.wav', 1024, fill_zeros=True)


def zero_crossing(ch_left, ch_right):
    zcr = np.array([])
    last_value = -1
    for i in ch_left:
        z_c = 0
        for j in range(int(i.shape[0])):
            if np.sign(i[j]) == 0:
                i[j] = -1
            if j == 0:
                if np.sign(last_value) != np.sign(i[j]):
                    z_c += 1
                continue
            if np.sign(i[j]) != np.sign(i[j-1]):
                z_c += 1
        last_value = i[j]
        zcr = np.append(zcr, z_c)


    print(np.sum(zcr, dtype=np.int16))
zero_crossing(left, right)
plt.plot(left.flat)
plt.show()


