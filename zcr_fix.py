from wave_to_array import wave_to_array
from sine_gen import sine_generator
import matplotlib.pyplot as plt
import numpy as np

#sine_generator(10.0, 1.0, 50, True)
sr, left, right = wave_to_array('sine_stereo_10.0_0.05kHz.wav', 2**11, fill_zeros=True)
print(left)
zcr = np.array([])
last_value = -1
for i in left:
    z_c = 0
    #print(i.shape)
    for j in range(int(i.shape[0])):
        #print(i[j])
        if np.sign(i[j]) == 0:
            i[j] = -1
        if j == 0:
            if np.sign(last_value) != np.sign(i[j]):
                z_c += 1
            continue

        if np.sign(i[j]) != np.sign(i[j-1]):
            z_c += 1
            #print(j)
    last_value = i[j]
    zcr = np.append(zcr, z_c)
print(zcr[0:])
print(2**14)
print(np.sum(zcr, dtype=np.int16))
#print(k)
plt.plot(zcr)
plt.show()


