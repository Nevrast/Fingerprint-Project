#moduł potrzebny do obsługi linii poleceń
import argparse

#import potrzebnych funkcji
from support_functions.wave_open import wave_open
from support_functions.windowing import windowing

from scipy.signal import stft

from parameters.zcr import zero_crossing
from parameters.energy_spectral_density import energy_spectral_denisity
from parameters.spectral_flatness import spectral_flatness
from parameters.spectral_centroid import spectral_centroid
from parameters.rms import rms



#opis skryptu
parser = argparse.ArgumentParser(description='This is a script which creates fingerprint matrix for specified input signal.')
#obowiązkowy argument dla wejściowego pliku
parser.add_argument("input", help = "- input signal")
#opcjonalny argument dla pliku wyjściowego
parser.add_argument("-o", "--output", help = "- output file")
#aby wywołać tryb debugujący należy wywołać tylko flagę -d bez żadnej wartości
parser.add_argument("-d", "--debug", help = "- debugging mode, this argument is called without any value", default = False, action = 'store_true')

#rozpakowanie parsera
args =parser.parse_args()
#wyświetla nazwy plików wejściowego i wyjściowego tylko w trybie debug
if args.debug:
    print("Input file: ", args.input)
INPUT_PATH = args.input

if args.output:
    if args.debug:
        print("Output file:", args.output)
    OUTPUT_PATH = args.output

def fing_creat(input):
    #wczytywanie pliku
    data, number_of_frames, channels, sampling_rate, duration = wave_open(input, normalize=True, rm_constant=True)
    left_channel, right_channel = windowing(data=data, sampling_rate=sampling_rate,
                                            channels=channels, window_size=2048, offset=0, to_mono=False,
                                            fill_zeros=True)
    #freq_bin to częstotliwości odpowiadające amplitudom w każdym oknie czasowym
    #time_bin to czasowe pozycje kolejnych okienek
    #magnitudes to trójwymiarowa macierz zawierająca dwa kanały, z których każdy składa się z N liczby
    #okien czasowych, gdzie każde okno czasowe to wektor amplitud kolejnych częstotliwośći
    freq_bin, time_bin, magnitudes = stft(data, fs=sampling_rate, window='hamming',
                                          nperseg=1024, noverlap=None)

    #to jest lista, do której zapisywane będą wszystkie parametry
    fprint = []

    # dodawanie kolejnych parametrów do listy
    # nazwy funkcji powinny być nazwą parametru
    # każda funkcja powinna przyjmować jako argument listę, która zawiera zokienkowany sygnał wejściowy,\
    # następnie wykonywać odpowiednie operacje i zwracać dany parametr\
    #do funkcji przekazany jest okienkowany sygnał

    fprint.append(zero_crossing(left_channel, right_channel))
    #jeśli zostanie podany argument -d, skrypt jest odpalony w trybie debugowania, więc wypisze wszystkie argumenty na ekran
    if args.debug:
        print(f"Zero_crossing_rate in fprint: {fprint[0]}\n\n")

    # fprint.append(energy_spectral_denisity(left_channel, right_channel))
    # if args.debug:
    #     print(f"Energy_spectral_denisity in fprint: {fprint[1]}\n\n")

    fprint.append(spectral_centroid(magnitudes=magnitudes, freq_bin=freq_bin))
    if args.debug:
        print(f"Spectral centroid in fprint: {fprint[2]}\n\n")

    fprint.append(spectral_flatness(magnitudes=magnitudes))
    if args.debug:
        print(f"Spectral flatness in fprint: {fprint[3]}\n\n")
    #
    # fprint.append(octave_fft(input_chunk))
    # if args.debug:
    #     print(f"octave_fft in fprint: {fprint[4]}\n\n")

    #zwraca naszą listę
    return fprint

def fing_save(fingerprint, output):
    if args.debug:
        print("Saving to file...")
    file = open(output, 'w')
    for elem in fingerprint:
        file.write(str(elem))
    file.close()
    if args.debug:
        print("Saving to file finished.")

#wywołanie funkcji i przypisanie do zmiennej new_fingerprint
new_fingerprint = fing_creat(INPUT_PATH)
#jeśli został podany argument -o zostanie wywołana funkcja zapisująca do pliku
if args.output:
    fing_save(new_fingerprint, OUTPUT_PATH)
