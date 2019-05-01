import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from support_functions import windowing, wave_read, fft
from scipy.signal import stft
np.set_printoptions(threshold=sys.maxsize)

# data, number_of_frames, channels, sampling_rate, duration =\
#     wave_read.wave_open("sine_mono_100.0_48.0kHz.wav")
data, number_of_frames, channels, sampling_rate, duration =\
     wave_read.wave_open("wnoise.wav")
# data, number_of_frames, channels, sampling_rate, duration =\
#      wave_read.wave_open("pnoise.wav")
# data, number_of_frames, channels, sampling_rate, duration =\
#     wave_read.wave_open("sine_stereo_10.0_0.05kHz.wav")
# data, number_of_frames, channels, sampling_rate, duration =\
#     wave_read.wave_open("sine_stereo_1000.0_44.1kHz.wav")
# data, number_of_frames, channels, sampling_rate, duration =\
#     wave_read.wave_open("sine_mono_1000.0_44.1kHz.wav")
#
# print(data)
# l, r=windowing.windowing(data, sampling_rate=sampling_rate,channels=channels)
freq_bin, time_bin, magnitudes = stft(data, fs=sampling_rate, window='hann',
                                      nperseg=512, noverlap=None)
def spectral_flatness(magnitudes):
    sf_left = np.array([])
    sf_right = np.array([])

    if len(magnitudes.shape) == 2:
        N = magnitudes.shape[0]
        for window in magnitudes.T:
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            sf_left = np.append(sf_left, flatness)
        sf_right = -1

    # elif len(magnitudes.shape) == 3:
    #     for window in magnitudes[0].T:
    #
    #     for window in magnitudes[1].T:

    else:
        raise ValueError("Input is not supported")

    return sf_left, sf_right
magnitudes = magnitudes.T
flatness, r = spectral_flatness(magnitudes)
print(flatness)
plt.plot(freq_bin, magnitudes[0])
plt.plot(freq_bin, magnitudes[1], 'r')
plt.xscale("log")
plt.show()