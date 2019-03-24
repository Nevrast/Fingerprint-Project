import wave
import struct


def wave_to_list(directory, split_into_chunks=True, window_size=64, offset=0):

    if window_size < 16:        # minimalne okienko 16 probek
        window_size = 16
    wave_file = wave.open(directory, 'r')  # otwarcie pliku w trybie readonly
    wave_length = wave_file.getnframes()  # dlugosc pliku

    values = []  # pusta lista na wartosci wave'a
    chunk_values = []  # lista na wartości chunków
    for i in range(0, wave_length):  # iteracja po calym pliku
        wave_data = wave_file.readframes(1)  # zapis do zmiennej typu bytes
        data = struct.unpack("<h", wave_data)  # zmiana z byte na tuple z intami
        values.append(int(data[0]))  # konwersja na liste intow
    values = normalize(values)
    print(max(values))
    # testowe values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    if split_into_chunks:
        if offset == 0:
            for i in range(0, len(values), window_size):  # ciecie listy w chunki o rozmiarze window_size
                chunk = values[i:i + int(window_size)]
                chunk_values.append(chunk)
        else:
            """
            TODO: Naprawic, nie działa poprawnie dla wszystkich przypadków
            """
            if offset >= 100:
                offset = 99
            offset = int(window_size*(100 - offset)/100)
            for i in range(0, len(values)):
                if i % offset == 0:
                    print(i)
                    chunk = values[i:i + int(window_size)]
                    chunk_values.append(chunk)
    wave_file.close()

    """zwraca listę oraz number_of_chunks list wartości wave'a"""
    return values, chunk_values


def normalize(values):
    """
    :param values: lista wartości wave'a
    :return: znormalizowana lista
    """
    maximum = max(values)
    normalized_values = []
    for value in values:
        normalized_value = value/maximum
        normalized_values.append(normalized_value)
    return normalized_values
