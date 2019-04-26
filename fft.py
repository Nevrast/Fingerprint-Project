from scipy.fftpack import fft
import numpy as np

def fft_function(ch_left, ch_right=None):

    fft_left = np.array([])
    fft_right = np.array([])

    for window in ch_left:
        fft_left = np.append(fft_left, fft(window), axis=0)

    # if type(ch_right) == type(ch_left):
    #     for window in ch_right:
    #         fft_right = np.append(fft_right, fft(np.array(window)))
    # else:
    #     fft_right = -1
    return fft_left, np.sum(fft_right)
"""
        input: 
    values ​​of the audio signal under test
        return: param 
    magnitude of the Fourier transform
"""


# ---------------TESTS---------------------------
#Testowe wywoałanie funkcji
import matplotlib.pyplot as plt
from wave_read import wave_open
from windowing import windowing

data, number_of_frames, channels, sampling_rate, duration = wave_open("sine_stereo_1000_44.1kHz.wav")
windows_l, windows_r = windowing(data, sampling_rate, channels)

fft_left, fft_right = fft_function(windows_l, windows_r)
print(fft_left)
# plt.plot(fft_left[0])
# plt.show()




