from wave_to_array import wave_to_array
from sine_gen import sine_generator
import matplotlib.pyplot as plt
import numpy as np

#sine_generator(100.0, 1.0, 40960, True)
sr, left, right = wave_to_array('sine_stereo_1000.0_44.1kHz.wav', 4096)
print(sr)

def crossings_nonzero_all(data):
    pos = data > 0
    npos = ~pos
    return ((pos[:-1] & npos[1:]) | (npos[:-1] & pos[1:])).nonzero()[0]
#print(right.shape)
k=[]
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
            print(i[j], i[j-1])
            print(z_c)
       # print(i[-1])
        #prev_value = i[j]
#print(i.shape)
    #zcr.put(crossings_nonzero_all(i))
    # for j in range(int(i.shape[0])):
    #     #print(i[j])
    #     zero_crossings = np.where(np.diff(np.signbit(i[j])))[0]
    #    # print(i[-1])
    #     #prev_value = i[j]
print(zcr.shape)
#print(k)
plt.plot(left[0])
plt.show()


