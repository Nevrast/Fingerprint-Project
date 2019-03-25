import numpy as np

"""
TODO: threshold for zcr trigger
"""


def zero_crossing_rate(input_singal=None, input_chunk=None):
    """
    :param input_singal: list, waveform values
    :param input_chunk: list2D, waveform split into chunks
    :return: Zero Crossing Rate of whole waveform or ZCR of every chunk
    """
    prev_value = 0  # przechowuje poprzednią wartość
    zero_crossing = 0  # liczba przejść przez zero

    if input_chunk is None:  # jeśli nie dostajemy okienek to robimy tylko zcr dla całego sygnału
        for value in input_singal:  # zwykla iteracja po wartościach
            if value * prev_value < 0 or value == 0:  # jeśli jest spelnione to nastąpiło ZC
                zero_crossing += 1
            prev_value = value  # zapis poprzedniej wartości

        return zero_crossing
    else:
        zero_crossing_in_chunk = []

        for i in range(len(input_chunk)):  # iteracja po liście okienek
            zero_crossing = 0  # resetowanie wartości ZC dla nowego okienka
            for j in input_chunk[i]:  # iteracja po i-tym okienku
                if j * prev_value < 0 or j == 0:  # jeśli jest spełnione to nastąpiło ZC
                    zero_crossing += 1
                prev_value = j  # zapis poprzedniej wartości
            zero_crossing_in_chunk.append(zero_crossing)  # dodanie przejść przez zero okna do listy

        return np.array(zero_crossing_in_chunk)

