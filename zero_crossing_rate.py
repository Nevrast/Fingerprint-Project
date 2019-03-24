import numpy as np

"""
TODO: threshold for zcr trigger
"""


def zero_crossing_rate(fingerprint, input_singal, input_chunk=None):
    """
    :param fingerprint: list, exsting fingerprint
    :param input_singal: list, waveform values
    :param input_chunk: list2D, waveform split into chunks
    :return: Zero Crossing Rate of whole waveform or ZCR of every chunk
    """
    prev_value = 0
    zero_crossing = 0
    chunk = []

    if input_chunk is None:
        for value in input_singal:
            if value * prev_value < 0 or value == 0:  # if this condition is fulfilled then
                zero_crossing += 1                    # there was zero crossing
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
                if value * prev_value < 0 or value == 0:
                    zero_crossing += 1
                prev_value = value
            zero_crossing_in_chunk.append(zero_crossing)

        fingerprint.append(zero_crossing_in_chunk)

        return np.array(fingerprint)

