import wave
import struct
import numpy as np


def wave_open(file_name):
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
    return data, number_of_frames, channels, sampling_rate, duration
