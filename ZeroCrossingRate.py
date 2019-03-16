import SineWaveGenReader


def zero_crossing_rate(file_name):
    prev_value = 0  # zmienna do przechowywania poprzedniej wartosci
    zero_crossing = 0
    wave_values = SineWaveGenReader.wave_to_list(file_name)  # lista z wartosciami pliku
    for value in wave_values:
        if value * prev_value < 0 or value == 0:  # jesli <= 0 to nastąpiło przejscie przez zero
            zero_crossing += 1
        prev_value = value
    return zero_crossing


print(zero_crossing_rate("sine_1300.0.wav"))
