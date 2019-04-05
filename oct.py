import wave_to_list, fft
import matplotlib.pyplot as plt
import numpy as np

wave_data, chunks, sample_rate = wave_to_list.wave_to_list("cello.wav", window_size=2048)

#print(chunks[0])
fy = fft.fft_function(chunks)
w = np.fft.fft(chunks[0])
frate = 44100.0

def octave_fft(wav_walues):
    octave = [16, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
    param = []

    for i in octave:

            lower_limit = int(i / 2 ** (1 / 2))
            upper_limit = int(i * 2 ** (1 / 2))
            lower_freq_index = int(lower_limit / (44100 / 2048))
            upper_freq_index = int(upper_limit / (44100 / 2048))
            #print(lower_freq_index, upper_freq_index)
            oct = fy[lower_freq_index:upper_freq_index]
            param.append(oct)

            #print (oct)
            #print(param)
    return param

print(octave_fft('cello.wav'))
