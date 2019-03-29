import numpy as np
import matplotlib.pyplot as plt
import wave_to_list_sine_gen
import fft

def energy_spectral_denisity(fft_list):
    #wzór na widmową gęstość energii: esp = (fft*sprzęrzenie zespolone fft)/(2*pi)
    con_fourier=[np.conjugate(values) for values in fft_list] #sprzężenie zespolone transformaty Fouriera
    esp = np.fft.fftshift([(a*b)/(2*np.pi) for a,b in zip(fft_list,con_fourier)]) #obliczanie widmowej gęstości energii ze wzoru
    return esp

    #--------------TESTS---------------------------
    N = len(wav_values)
    plt.plot(np.arange(-N/2, N/2, dtype=float) / N, esp)
    plt.xlim(-0.5, 0.5)
    plt.title('Spectrum')
    print (0)
    plt.ylabel('Squared modulus')
    plt.xlabel('Normalized Frequency')
    plt.grid()
    plt.show()
#--------------TESTS---------------------------
wav_values, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_1000.0.wav", False, 44100)
#print(wav_values) 
fft_list = fft.fft_function(wav_values)
energy_spectral_denisity(fft_list)