import wave_to_array
import numpy as np


def zero_crossing_rate(file_name, split_into_chunks):
    prev_value = 0  # zmienna do przechowywania poprzedniej wartosci
    zero_crossing = 0
    wave_values, wave_chunks = wave_to_array.wave_to_list(file_name, split_into_chunks, 5)  # lista z wartosciami pliku
    chunk_array = []
    chunk = []

    if not split_into_chunks:
        for value in wave_values:
            if value * prev_value < 0 or value == 0:  # jesli <= 0 to nastąpiło przejscie przez zero
                zero_crossing += 1
            prev_value = value
        return zero_crossing  # zwraca zrc w postaci jednego inta
    else:
        zero_crossing_in_chunk = []
        for i in range(len(wave_chunks)):
            chunk.clear()
            zero_crossing = 0
            for j in wave_chunks[i]:
                chunk.append(j)
            for value in chunk:
                if value * prev_value < 0 or value == 0:  # jesli <= 0 to nastąpiło przejscie przez zero
                    zero_crossing += 1
                prev_value = value
            zero_crossing_in_chunk.append(zero_crossing)
            chunk_array.append(chunk)
        return np.array(zero_crossing_in_chunk)  # zwraca numpy.ndarray przejść przez zero


print(zero_crossing_rate("sine_1300.0.wav", True))
print(zero_crossing_rate("sine_1300.0.wav", False))
