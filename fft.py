from scipy.fftpack import fft
import numpy as np
import wave_to_list
import matplotlib.pyplot as plt

wav_values, wav_values_chunks = wave_to_list.wave_to_list("in_the_element.wav", False)
print(type(wav_values))
N = len(wav_values)
print(N)
T = 1.0/N
x = np.linspace(0.0, N*T, N)
y = np.array(wav_values)
#y = np.sin(50*2.0*np.pi*x)+0.5*np.sin(80.0*2.0*np.pi*x)
print(type(y))
yf = fft(y)
print(len(yf))
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
