import wave
import struct
import math


def sine_generator(name, freq, duration=10.0, sample_rate=44100.0):
    values = []
    wave_file = wave.open(name + ".wav", 'w')

    wave_file.setnchannels(1)  # mono
    wave_file.setsampwidth(2)
    wave_file.setframerate(sample_rate)

    for i in range(int(duration * sample_rate)):
        value = int(32767.0 * math.sin(freq * 2.0 * math.pi * float(i) / float(sample_rate)))
        values.append(value)
        data = struct.pack('<h', value)
        wave_file.writeframesraw(data)

    wave_file.close()
    return values


def wave_to_list(directory):
    wave_file = wave.open(directory, 'r')
    wave_length = wave_file.getnframes()
    list_t = []
    for i in range(0, wave_length):
        wave_data = wave_file.readframes(1)
        data = struct.unpack("<h", wave_data)
        list_t.append(int(data[0]))
    return list_t


sine_generator("halo_wyspa", 1300.0, 1.0, 44100.0)
