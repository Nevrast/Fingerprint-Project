import wave
import struct
import numpy as np

def wave_read(file_name):
    # wave_file = wave.open(file_name, 'rb')
    # channels = wave_file.getnchannels()
    # sample_freq = wave_file.getframerate()
    # if channels == 1:
    #     mono = []
    #     for frame in range(0, wave_file.getnframes()):
    #         wave_data = wave_file.readframes(1)
    #         data = struct.unpack("<h", wave_data)
    #         mono.append(data[0])
    # print(mono)
    # if channels == 2:
    #     left = []
    #     right = []
    #     for frame in range(0, wave_file.getnframes()):
    #         wave_data = wave_file.readframes(1)
    #         data = struct.unpack("<hh", wave_data)
    #         left.append(data[0])
    #     print(sum(left))
    #     for frame in range(1, wave_file.getnframes()):
    #         wave_data = wave_file.readframes(1)
    #         data = struct.unpack("<hh", wave_data)
    #         right.append(data[0])
    #     print(sum(right))
    wave_file = wave.open(file_name, 'r')
    nframes = wave_file.getnframes()
    nchannels = wave_file.getnchannels()
    sampling_frequency = wave_file.getframerate()
    T = nframes / float(sampling_frequency)
    read_frames = wave_file.readframes(nframes)
    wave_file.close()
    data = struct.unpack("%dh" % nchannels * nframes, read_frames)
    return T, data, nframes, nchannels, sampling_frequency

# print(wave_read("sine_1000.0.wav"))
T, data, nframes, nchannels, sampling_freq = wave_read("sine_stereo_100.0_44.1kHz.wav")
left = data[0:50:2]
right = data[1:50:2]
array = np.array(left)
print(left)
print(array)


