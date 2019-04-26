from scipy.fftpack import fft
import numpy as np

def fft_function(wav_values):
    param = []
    for window in wav_values:
        param.append(fft(np.array(window)))
    return param
"""
        input: wav_values
    values ​​of the audio signal under test
        return: param 
    magnitude of the Fourier transform

"""

# ---------------TESTS---------------------------
#wyświetlanie wykresu, by sprawdzić, czy funckja działa poprawnie
# import wave_to_list_sine_gen
# import matplotlib.pyplot as plt
#
# wave_to_list_sine_gen.sine_generator(50000.0, 1)
# signal, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_50000.0.wav", False, 44100)
#
# y = fft_function(signal)
#
# N = len(signal)  # liczba próbek
# T = 1.0 / 44100  # okres
#
# xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)  # plot
# plt.plot(xf, 2.0 / N * np.abs(y[0:N // 2]))
# plt.show()"""

# ---------------TESTS---------------------------
#Testowe wywoałanie funkcji
#import wave_to_list_sine_gen
#import matplotlib.pyplot as plt

#wave_to_list_sine_gen.sine_generator(50000.0, 1)
#signal, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_50000.0.wav", False, 44100)

#y = fft_function(signal)

#N = len(signal)  # liczba próbek
#T = 1.0 / 44100  # odległość próbek

#xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)  # plot
#plt.plot(xf, 2.0 / N * np.abs(y[0:N // 2]))
#plt.show()"""
