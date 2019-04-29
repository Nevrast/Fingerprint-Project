from scipy.signal import stft
from .windowing import windowing
from .wave_read import wave_open
import matplotlib.pyplot as plt
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# data, number_of_frames, channels, sampling_rate, duration = wave_open("sine_1000.wav")
data, number_of_frames, channels, sampling_rate, duration = wave_open("sine_stereo_100.0_44.1kHz.wav")
left, right = windowing(data,channels=channels, window_size=2048,sampling_rate=sampling_rate, fill_zeros=False)
f, t, Zxx = stft(left.flatten(), sampling_rate, window='hamming', nperseg=2048)
# amp = 2 * np.sqrt(2)
# plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)

print(t.shape)
print(Zxx.shape)
# Zxx= Zxx.T
f = f.astype(np.int16)
print(f[::])
plt.title('STFT Magnitude')
plt.plot(f, np.abs(Zxx))
plt.axis(xmin=0,xmax=1000)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
