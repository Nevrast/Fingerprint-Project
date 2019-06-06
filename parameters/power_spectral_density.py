# import scipy.signal as sl
# import matplotlib.pyplot as plt
#
# def power_spectral_density(window_left, window_right, sampling_rate, window):
#     freqs_left, power_spectral_left = sl.periodogram(window_left, fs=sampling_rate, window=window, nfft=8192)
#     freqs_right, power_spectral_right = sl.periodogram(window_right, fs=sampling_rate, window=window, nfft=8192)
#
#
#     return power_spectral_left, power_spectral_right
#
# def power_spectral_debug():
#     # # print(freqs)
#     # # print(power_spectral)
#     # # print("freqs size ", freqs.size)
#     # # print("freqs shape ", freqs.shape)
#     # # print("size ", power_spectral.size)
#     # # print("shape ", power_spectral.shape)
#     # # print("type", type(power_spectral))
#     # # print(number_of_frames/2048)
#
#     # plt.semilogx(freqs, power_spectral[100], freqs, power_spectral[0])
#     # # freqs.reshape(power_spectral.shape)
#     # # plt.semilogx(freqs, power_spectral)
#     # # print(freqs[0:50])
#     # plt.xlim(left = freqs[1])
#     # #plt.show()
#     #
#     # # f_welch, power_welch = sl.welch(data)
#     # #
#     # # plt.semilogx(f_welch, power_welch)
#     # plt.show()
#     pass

import scipy.signal as sl
import matplotlib.pyplot as plt
from support_functions.wave_open import wave_open
from support_functions.windowing import windowing
import numpy as np
from copy import copy
window_size = 1024
offset = 512
window = 'hann'
#sine_stereo_100.0_48.0kHz.wav
data, number_of_frames, channels, sampling_rate, duration = wave_open('sine_stereo_100.0_48.0kHz.wav', normalize=True, rm_constant=True)
left_channel, right_channel, w_time_bin = windowing(data=data, sampling_rate=sampling_rate, channels=channels,
                                                        window_size=window_size, offset=offset, to_mono=False,
                                                        fill_zeros=True)

def power_spectral_density(window_left, window_right, sampling_rate, window):
    av_psd_l = np.array([])
    av_psd_r = np.array([])
    print(window_right, window_left)
    freqs_left, power_spectral_left = sl.periodogram(window_left, fs=sampling_rate, window=window, nfft=window_left.shape[-1])
    for window in power_spectral_left:
        av_psd_l = np.append(av_psd_l, np.max(window))

    freqs_right, power_spectral_right = sl.periodogram(window_right, fs=sampling_rate, window=window, nfft=window_right.shape[-1])

    return power_spectral_left, power_spectral_right
l, r = power_spectral_density(window_left=left_channel, window_right=right_channel, sampling_rate=sampling_rate, window='hann')

print(l.shape)