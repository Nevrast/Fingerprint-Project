from scipy.fftpack import fft
import wave_to_list
import numpy as np
import matplotlib.pyplot as plt

input_chunk, input_chunk = wave_to_list.wave_to_list("in_the_element.wav", window_size=64)



def spectral_centroid(input_chunk, samplerate=44100):
    param = []
    for i in range(len(input_chunk)):
        N = len(input_chunk[i])
        magnitudes = np.abs(np.fft.rfft(input_chunk[i]))
        length = len(input_chunk[i])
        freqs = np.abs(np.fft.fftfreq(length, 1.0/samplerate)[:length//2+1])
        param.append((magnitudes*freqs) / np.sum(magnitudes))
        #print(freqs)
    return param #

print(spectral_centroid(input_chunk))
