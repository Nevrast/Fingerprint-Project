import numpy as np
import matplotlib.pyplot as plt
import wave_to_list_sine_gen
import fft

#calculation from the formula
def energy_spectral_denisity(fft_list):
    con_fourier=[np.conjugate(values) for values in fft_list] #conjugated complex Fourier transforms
    esp = np.fft.fftshift([(a*b)/(2*np.pi) for a,b in zip(fft_list,con_fourier)])
    print (esp[0:3])

    # calculation by definition - not finished:
    #dsp1 = np.fft.fftshift(np.abs(np.fft.fft(np.array(wav_values))) ** 2)
    #print(dsp1[0:3])
    #--------------TESTS---------------------------
    """N = len(wav_values)
    plt.plot(np.arange(-N/2, N/2, dtype=float) / N, dsp1)
    plt.xlim(-0.5, 0.5)
    plt.title('Spectrum')
    print (0)
    plt.ylabel('Squared modulus')
    plt.xlabel('Normalized Frequency')
    plt.grid()
    plt.show()"""

wav_values, wav_values_chunks = wave_to_list_sine_gen.wave_to_list("sine_1000.0.wav", False, 44100)
#print(wav_values) #test
fft_list = fft.fft_function(wav_values)
energy_spectral_denisity(fft_list)