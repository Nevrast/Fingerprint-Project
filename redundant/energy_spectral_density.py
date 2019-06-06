import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft as stft

def energy_spectral_denisity(magnitudes):
    """
    :param left_list: array, magnitude of fft in left channel
    :param right_list: array, magnitude of fft in right channel
    :return: list, values of energy spectral density
    """
#lewy kanał
    #wzór na widmową gęstość energii: esp = (fft*sprzężenie zespolone fft)/(2*pi)
    # left_stft = np.array(stft(left_list))
    # con_fourier_left = np.conjugate(left_stft) #sprzężenie zespolone transformaty Fouriera
    # esp_left = np.fft.fftshift([(a*b)/(2*np.pi) for a,b in zip(left_list, con_fourier_left)]) #obliczanie widmowej gęstości energii ze wzoru
    left = magnitudes[0]
    left_con=np.conjugate(left)
    #esp_left = left*left_con / (2*np.pi)
    esp_left = np.fft.fftshift([(a*b)/(2*np.pi) for a,b in zip(left, left_con)])

#prawy kanał
    right = magnitudes[1]
    #if sprawdza czy w ogóle drugi kanał istnieje
    if right is not None:
        right_con=np.conjugate(left)
    #esp_left = left*left_con / (2*np.pi)
        esp_right = np.fft.fftshift([(a*b)/(2*np.pi) for a,b in zip(right, right_con)])
    #jeśli nie istnieje to też zwraca parametr dla drugiego kanału
    else:
        esp_right = 0

#to jeszcze do poprawy
    #--------------TESTS---------------------------
    #wykres wyświetlany, aby sprawdzić, czy funckja liczy właście wartości
    #N = len(wav_values)
    #plt.plot(np.arange(-N / 2, N / 2, dtype=float) / N, abs(esp))
    #plt.xlim(-0.5, 0.5)
    #plt.title('Spectrum')
    #print(0)
    #plt.ylabel('Squared modulus')
    #plt.xlabel('Normalized Frequency')
    #plt.grid()
    #plt.show()
    # --------------END-TESTS---------------------------
    return esp_left, esp_right

#--------------TESTS---------------------------
#wywoaływanie funkcji, aby sprawdzić, czy funkcja działa poprawnie
#wav_values, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_10000.0.wav", False, 44100)
#fft_list = fft.fft_function(wav_values)
#print(energy_spectral_denisity(fft_list))
