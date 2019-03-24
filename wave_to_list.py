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
        window_size = 16  # minimum window size
    wave_file = wave.open(file_name, 'r')
    wave_length = wave_file.getnframes()

    values = []
    chunk_values = []

    for i in range(0, wave_length):  # converts bytes to list of integer values
        wave_data = wave_file.readframes(1)
        data = struct.unpack("<h", wave_data)
        values.append(int(data[0]))

    values = normalize(values)  # normalizes values

    if split_into_chunks:  # splits values into even chunks and creates
        if offset == 0:    # list depending on input
            for i in range(0, len(values), window_size):
                chunk = values[i:i + int(window_size)]
                chunk_values.append(chunk)
        else:
            chunk_values.append(overlap(values, window_size, offset, chunk_values))
            del chunk_values[-1]  # this has to be here because last element is always None

    wave_file.close()

    return values, chunk_values


def overlap(values, window_size, offset, chunk_values, start=0):
    """
    :param values: list, values of wave file
    :param window_size: int, size of single window
    :param offset: int, defines how much windows are overlapping
    :param chunk_values: list, place to store windows
    :param start: int, starting index of values
    :return: None
    """
    overlap_size = int(window_size*offset/100)  # converts offset from % to value based on window size

    while start <= len(values) - overlap_size:
        chunk_values.append(values[start:start + window_size])
        start += window_size - overlap_size


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
