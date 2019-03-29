import math
import wave_to_list
import sine_gen

"""
TODO: support for windowed signal, documentation, clean up code
"""


def rms(wave_list):
    squares = 0
    for value in wave_list:
        temporary = value**2
        squares = temporary + squares
    n = len(wave_list)
    t = squares/n

    return math.sqrt(t)


sine_gen.sine_generator(1000, 1.0)
sine_gen.sine_generator(10.0, 5.0, 40)
wave_list, chunks = wave_to_list.wave_to_list("sine_1000.0.wav", False)
print(rms(wave_list))
#print(wave_to_list.wave_to_list("sine_10.0.wav", True, 10))
