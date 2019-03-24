import wave_to_list
import numpy as np


def zero_crossing_rate(fingerprint, input_singal, input_chunk=None):
    """
    :param fingerprint: list, istniejący fingerprint do ktorego dorzucamy parametry
    :param input_singal: list, wartości wave'a
    :param input_chunk: lista2D, wartości wave'a podzielone na sublisty
    :return: zero crossing rate calego wave'a lub array zcr chunkow
    """
    prev_value = 0  # zmienna do przechowywania poprzedniej wartosci
    zero_crossing = 0
    chunk = []

    if input_chunk is None:
        for value in input_singal:
            if value * prev_value < 0 or value == 0:  # jesli <= 0 to nastąpiło przejscie przez zero
                zero_crossing += 1
            prev_value = value
        fingerprint.append(zero_crossing)
        return fingerprint
    else:
        zero_crossing_in_chunk = []
        for i in range(len(input_chunk)):
            chunk.clear()
            zero_crossing = 0
            for j in input_chunk[i]:
                chunk.append(j)
            for value in chunk:
                if value * prev_value < 0 or value == 0:  # jesli <= 0 to nastąpiło przejscie przez zero
                    zero_crossing += 1
                prev_value = value
            zero_crossing_in_chunk.append(zero_crossing)
        fingerprint.append(zero_crossing_in_chunk)
        return np.array(fingerprint)  # zwraca numpy.ndarray przejść przez zero

