from wave_to_array import wave_to_array
from sine_gen import sine_generator
import matplotlib.pyplot as plt
import numpy as np

#sine_generator(100.0, 1.0, 44100, True)
sr, left, right = wave_to_array('sine_stereo_100.0_44.1kHz.wav', 4096)
print(sr)




prev_value = 0

zcr = np.array([])
for i in left:
    # i= left[0]
    z_c = 0
    #print(i.shape)
    for j in range(int(i.shape[0])):
        #print(i[j])
        if i[j-1] == i[-1]:
            continue
        if np.sign(i[j]) == 0:
            i[j] = -1
        if np.sign(i[j]) != np.sign(i[j-1]):
            z_c += 1

            #print(i[j], i[j-1])
    #print(z_c)
    zcr = np.append(zcr, z_c)
# print(i[-1])
# prev_value = i[j]
# print(i.shape)
    #zcr.put(crossings_nonzero_all(i))
    # for j in range(int(i.shape[0])):
    #     #print(i[j])
    #     zero_crossings = np.where(np.diff(np.signbit(i[j])))[0]
    #    # print(i[-1])
    #     #prev_value = i[j]
print(np.sum(zcr, dtype=np.int16))
#print(k)
plt.plot(left[2])
plt.show()


