import math


#from ..support_functions.sine_gen import sine_generator

def rms(input_chunks):

    """
    :param input_chunks: list 2D, waveform split into chunks
    :return: rms of signal in chunks
    """
    parameters = []
    for i in range(len(input_chunks)):  # iteracja po elementach głównej listy
        squares = 0  # zmienna do przechowania kwadratów wartości
        for value in input_chunks[i]:  # iteracja po warościach elementów listy
            temporary = value**2  # potęga wartości
            squares = temporary + squares  # sumowanie kwadratów
        n = len(input_chunks[i])  # długość podlisty
        t = squares/n  # suma kwadratów podzielona przez długość podlisty
        parameters.append(math.sqrt(t))  # dodawanie pierwiastka z t do listy parametrów

    return parameters


""" TEST
sine_gen.sine_generator(1000, 1.0)
sine_gen.sine_generator(10.0, 5.0, 40)
wave_list, chunks = wave_to_list.wave_to_list("sine_1000.wav", True,window_size = 2048)
print(rms(chunks))
#print(wave_to_list.wave_to_list("sine_10.0.wav", True, 10))
"""
