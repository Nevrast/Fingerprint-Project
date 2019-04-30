from scipy.signal import stft
from scipy.fftpack import fft
from windowing import windowing
from wave_read import wave_open
import matplotlib.pyplot as plt
import numpy as np
import scipy
import sys
# np.set_printoptions(threshold=sys.maxsize)

# data, number_of_frames, channels, sampling_rate, duration = wave_open("sine_1000.wav")
data, number_of_frames, channels, sampling_rate, duration =\
    wave_open(r"D:\Studies\Sem6\Projekt Dolby\Repository\sine_stereo_100.0_44.1kHz.wav")
left, right = windowing(data,channels=channels, window_size=512,sampling_rate=sampling_rate, fill_zeros=False)
left_l, right_l = windowing(data,channels=channels, window_size=4096,sampling_rate=sampling_rate, fill_zeros=False)

# fft_s =np.abs(scipy.fftpack.rfft(left[6]))

# fft_l = np.abs(scipy.fftpack.rfft(left.flatten()))
# print(fft_s.shape, fft_l.shape)
flat_left = left.flatten()
data_l = data[::2]

f, t, Zxx = stft(data, sampling_rate, window='hamming', nperseg=2048)
# fft = np.abs(fft(flat_left))
# # amp = 2 * np.sqrt(2)
# # plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
print(f.shape)
print(t.shape)
print(Zxx.shape)
print(data.shape)
# # Zxx= Zxx.T
# f = f.astype(np.int16)
# freqs_l =np.fft.rfftfreq(2048, 1/44100)
# freqs_s =np.fft.rfftfreq(512, 1/44100)
# print(freqs_l.shape, freqs_s.shape)
# # print(freqs.astype(np.int16))
# print(f[::])
plt.title('STFT Magnitude')
# plt.plot(f, np.abs(Zxx))
# plt.plot( fft_s, 'b')
# plt.plot(fft_l, 'r')
# plt.axis(xmin=0,xmax=50)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
# plt.show()
