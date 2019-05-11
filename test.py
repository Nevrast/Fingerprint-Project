from support_functions.wave_open import wave_open
import numpy as np
from scipy.signal import stft
data, number_of_frames, channels, sampling_rate, duration = wave_open(r'sine_mono_1000_44.1kHz.wav', normalize=True, rm_constant=True)
freq_bin, time_bin, magnitudes = stft(data, fs=sampling_rate, window='hamming', nperseg=1024, noverlap=None, boundary=None)

def spectral_flux(magnitudes):
    sf_left = 0
    sf_right = 0

    '''
    input: magnitudes of the STFT
    output: spectral flux of tested signal
    '''

    if len(magnitudes.shape) == 2: #oblicznie dla dźwięków mono
        for window in magnitudes.T:
            normalized_magnitude =  np.array([])
            nm = np.abs(window) / np.max(np.abs(window)) #obliczanie znormalizowanych wartości amplitud
            normalized_magnitude = np.append (normalized_magnitude, nm)
            for i in range(0, len(normalized_magnitude)):
                df = np.int(normalized_magnitude[i]) - np.int(normalized_magnitude[i-1]) #obliczenie spectral flux ze wzoru
                sf_left = sf_left + (df**2)
                sf_right = -1

    elif len(magnitudes.shape) == 3: #obliczanie dla dźwięków stero
        for window in magnitudes[0].T:
            normalized_magnitude =  np.array([])
            nm = np.abs(window) / np.max(np.abs(window))
            normalized_magnitude = np.append (normalized_magnitude, nm)
            for i in range(0, len(normalized_magnitude)):
                df = np.int(normalized_magnitude[i]) - np.int(normalized_magnitude[i-1])
                sf_left = sf_left + (df**2)

        for window in magnitudes[1].T:
            normalized_magnitude =  np.array([])
            nm = np.abs(window) / np.max(np.abs(window))
            normalized_magnitude = np.append (normalized_magnitude, nm)
            for i in range(0, len(normalized_magnitude)):
                df = np.int(normalized_magnitude[i]) - np.int(normalized_magnitude[i-1])
                sf_right = sf_right + (df**2)
    else:
        raise ValueError("Input is not supported")

    return sf_left, sf_right


spectral_flux(magnitudes)