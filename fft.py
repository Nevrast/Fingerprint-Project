from scipy.fftpack import fft
import numpy as np
import wave_to_list_sine_gen

wav_values, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_22000.0.wav", False, 44100)
print(type(wav_values))
N = len(wav_values)
print(N)
T = 1.0/N
x = np.linspace(0.0, N*T, N)
y = np.array(wav_values)
#y = np.sin(50*2.0*np.pi*x)+0.5*np.sin(80.0*2.0*np.pi*x)
print(type(y))
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
