import wave
import struct

"""
TODO: check if overlapping works for every case
"""


def wave_to_list(file_name, split_into_chunks=True, window_size=64, offset=0):
    """
    :param file_name: string, file name
    :param split_into_chunks: bool, should file be split into chunks
    :param window_size: int, size of single window
    :param offset: int, defines how much windows are overlapping
    :return: list, list2D - returns normalized values of wave files and values split
                            into chunks
    """
    if window_size < 16:
        window_size = 16  # minimalny rozmiar okna
    wave_file = wave.open(file_name, 'r')  # otawrcie pliku read-only
    wave_length = wave_file.getnframes()  # długość pliku, int
    wave_channels = wave_file.getnchannels()  # liczba kanałów
    values = []  # pusta lista na wartości pliku
    chunk_values = []  # pusta lista na podlisty wartości pliku

    for i in range(0, wave_length):  # iteracja od 0 do długości pliku
        wave_data = wave_file.readframes(1)  # odczytywanie pliku w postaci byte
        if wave_channels == 1:
            data = struct.unpack("<h", wave_data)  # rozpakowywanie pliku i przygotowanie do zamiany na int
        else:
            data = struct.unpack("<hh", wave_data) # rozpakowywanie pliku i przygotowanie do zamiany na int
        values.append(int(data[0]))  # zamiana z byte na int
    values = normalize(values)  # normalizowanie listy do przedziału [1:-1]

    if split_into_chunks:  # jesli argument jest True to robimy podział na okna
        if offset == 0:    # jeśli offset jest 0 okienka sie nie nakładają
            for i in range(0, len(values), window_size):  # iteracja po liście wartości co długość okna
                chunk = values[i:i + int(window_size)]  # "cięcie" głównej listy na okna
                chunk_values.append(chunk)  # dodwanie okienek na koniec głównej listy
        else:  # jeśli chcemy żeby okna nachodziły na siebie o offset
            chunk_values.append(overlap(values, window_size, offset, chunk_values))
            del chunk_values[-1]  # na koncu listy jest None wiec trzeba go usunąć

    wave_file.close()  # WAŻNE - zamknięcie pliku

    return values, chunk_values, wave_file.getframerate()


def overlap(values, window_size, offset, chunk_values, start=0):
    """
    :param values: list, values of wave file
    :param window_size: int, size of single window
    :param offset: int, defines how much windows are overlapping
    :param chunk_values: list, place to store windows
    :param start: int, starting index of values
    :return: None
    """
    overlap_size = int(window_size*offset/100)  # zamiana wartosci w % na liczbę próbek zależną od okna

    while start <= len(values) - overlap_size:  # wykonuje się dopóki długość listy - wielkość overlapu są mniejsze
        # lub równe indexowi zaczynającemu podlistę
        chunk_values.append(values[start:start + window_size])  # cięcie listy na okna przesunięte o offset
        start += window_size - overlap_size  # zwiększanie indexu


def normalize(values):
    """
    :param values: values of wave file
    :return: normalized list
    """
    maximum = max(values)  # przechowuje max wartość listy
    minimum = abs(min(values))  # przechowuje max absolutną wartość listy
    normalized_values = []  # tablica na znormalizowane wartości

    for value in values:  # iteracja po głównej liście
        normalized_value = value/max(maximum, minimum)  # pojedyncza znormalizowana próbka
        normalized_values.append(normalized_value)  # przypisanie znormalizowanej próbki do listy

    return normalized_values
