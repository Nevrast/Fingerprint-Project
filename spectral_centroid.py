from scipy.fftpack import fft
import wave_to_list
import numpy as np
import matplotlib.pyplot as plt
import librosa

input_chunk, input_chunk = wave_to_list.wave_to_list("sine_1000.0.wav", window_size=4096)


def spectral_centroid(input_chunks, samplerate=44100):
    param = []
    for i in range(len(input_chunks)):
       # N = len(input_chunks[i])
        magnitudes = np.abs(np.fft.rfft(input_chunks[i]))
        length = len(input_chunks[i])
        freqs = np.abs(np.fft.fftfreq(length, 1.0/samplerate)[:length//2+1])
        print(freqs)
        param.append(np.sum((magnitudes*freqs)) / np.sum(magnitudes))
        #print(freqs)
    return param


for i in range(len(input_chunk)):
    param = []
    param.append(librosa.feature.spectral_centroid(np.array(input_chunk[i]), sr=44100))
   # print(param)
print(spectral_centroid(input_chunk))
