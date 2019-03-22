import wave
import struct
import math


def sine_generator(freq, duration=10.0, sample_rate=44100.0):
    values = []  # pusta lista na wartości wave'a

    wave_file = wave.open("sine_" + str(freq) + ".wav", 'w')  # otwarcie wave'a
    wave_file.setnchannels(1)  # mono
    wave_file.setsampwidth(2)  # liczba bitow na których zapisana jest próbka
    wave_file.setframerate(sample_rate)  # ustawienie f.probkowania

    for i in range(int(duration * sample_rate)):  # iteracja o dlugosci wave'a
        value = int(32767.0 * math.sin(freq * 2.0 * math.pi * float(i) / float(sample_rate)))  # robienie sinusa
        values.append(value)  # tworzenie listy z wartosciami do pozniejszego użytku
        data = struct.pack('<h', value)  # konwersja z int na byte
        wave_file.writeframesraw(data)  # zapis do wav
    wave_file.close()
    return values
