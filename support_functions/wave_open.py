import wave
import struct
import numpy as np


def wave_open(file_name, normalize=True, rm_constant=False):
    wave_file = wave.open(file_name, 'rb')

    number_of_frames = wave_file.getnframes()
    channels = wave_file.getnchannels()
    sampling_rate = wave_file.getframerate()
    duration = number_of_frames / float(sampling_rate)
    read_frames = wave_file.readframes(number_of_frames)

    wave_file.close()

    data = struct.unpack("%dh" % channels * number_of_frames, read_frames)

    if channels == 1:
        data = np.array(data, dtype=np.int16)

    elif channels == 2:
        left = np.array(data[0::2], dtype=np.int16)
        right = np.array(data[1::2], dtype=np.int16)
        data = np.vstack((left, right))

    else:
        raise ValueError("Unsupported number of channels")

    if normalize:
        data = np.divide(data, np.iinfo(np.int16).max + 1)

    if rm_constant and channels == 1:
        data = data - np.sum(data) / number_of_frames

    elif rm_constant and channels == 2:
        data[0] = data[0] - np.sum(data[0]) / number_of_frames
        data[1] = data[1] - np.sum(data[1]) / number_of_frames

    return data, number_of_frames, channels, sampling_rate, duration
