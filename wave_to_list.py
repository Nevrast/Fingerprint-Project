import wave
import struct


def wave_to_list(directory, split_into_chunks=True, number_of_chunks=1):

    if number_of_chunks < 1:
        number_of_chunks = 1
    wave_file = wave.open(directory, 'r')  # otwarcie pliku w trybie readonly
    sample_freq = wave_file.getframerate()
    wave_length = wave_file.getnframes()  # dlugosc pliku
    values = []  # pusta lista na wartosci wave'a
    chunk_values = []
    for i in range(0, wave_length):  # iteracja po calym pliku
        wave_data = wave_file.readframes(1)  # zapis do zmiennej typu bytes
        data = struct.unpack("<hh", wave_data)  # zmiana z byte na tuple z intami
        values.append(int(data[0]))  # konwersja na liste intow

    if split_into_chunks:
        for i in range(0, len(values), int(sample_freq/number_of_chunks)):
            chunk = values[i:i + int(sample_freq/number_of_chunks)]
            chunk_values.append(chunk)
    """zwraca listę lub number_of_chunks list wartości wave'a"""
    return values, chunk_values



