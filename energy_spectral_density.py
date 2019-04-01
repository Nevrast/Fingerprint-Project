import numpy as np
import matplotlib.pyplot as plt
#import wave_to_list_sine_gen
#import fft

def energy_spectral_denisity(fft_list):
    """
    :param fft_list: array, magnitude of fft
    :return: list, values of energy spectral density
    """
    #wzór na widmową gęstość energii: esp = (fft*sprzęrzenie zespolone fft)/(2*pi)
    con_fourier=[np.conjugate(values) for values in fft_list] #sprzężenie zespolone transformaty Fouriera
    esp = np.fft.fftshift([(a*b)/(2*np.pi) for a,b in zip(fft_list,con_fourier)]) #obliczanie widmowej gęstości energii ze wzoru

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
    return esp

#--------------TESTS---------------------------
#wywoaływanie funkcji, aby sprawdzić, czy funkcja działa poprawnie
#wav_values, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_1000.0.wav", False, 44100)
#fft_list = fft.fft_function(wav_values)
#print(energy_spectral_denisity(fft_list))
