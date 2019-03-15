import SineWaveGenReader


def zero_crossing_rate(file_name):
    prev_value = 0
    zero_crossing = 0
    wave_values = SineWaveGenReader.wave_to_list(file_name)
    for i in wave_values:
        value = i
        if i * prev_value < 0 or value == 0:
            zero_crossing += 1
        prev_value = value
    return zero_crossing


print(zero_crossing_rate("sinus_440.wav"))
