import scipy.signal as sl
import support_functions.wave_open as wave_open
import matplotlib.pyplot as plt
import support_functions.windowing as windowing

def power_spectral_density(window_left, window_right, sampling_rate, window):
    freqs_left, power_spectral_left = sl.periodogram(window_left, fs=sampling_rate, window=window, nfft=8192)
    freqs_right, power_spectral_right = sl.periodogram(window_right, fs=sampling_rate, window=window, nfft=8192)

    # print(freqs)
    # print(power_spectral)
    # print("freqs size ", freqs.size)
    # print("freqs shape ", freqs.shape)
    # print("size ", power_spectral.size)
    # print("shape ", power_spectral.shape)
    # print("type", type(power_spectral))
    # print(number_of_frames/2048)
    plt.semilogx(freqs, power_spectral[100], freqs, power_spectral[0])
    # freqs.reshape(power_spectral.shape)
    # plt.semilogx(freqs, power_spectral)
    # print(freqs[0:50])
    plt.xlim(left = freqs[1])
    #plt.show()

    # f_welch, power_welch = sl.welch(data)
    #
    # plt.semilogx(f_welch, power_welch)
    plt.show()

    return power_spectral_left, power_spectral_right
