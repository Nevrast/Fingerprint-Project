#moduł potrzebny do obsługi linii poleceń
import argparse

#import potrzebnych funkcji
from wave_to_list import wave_to_list
from zero_crossing_rate import zero_crossing_rate
from energy_spectral_density import energy_spectral_denisity
from rms import rms
from spectral_centroid import spectral_centroid
from oct import octave_fft

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
    #input_chunk to zokienkowany sygnał
    input_signal, input_chunk, sampling_rate = wave_to_list(input, window_size=2048)

    #to jest lista, do której zapisywane będą wszystkie parametry
    fprint = []

    # dodawanie kolejnych parametrów do listy
    # nazwy funkcji powinny być nazwą parametru
    # każda funkcja powinna przyjmować jako argument listę, która zawiera zokienkowany sygnał wejściowy,\
    # następnie wykonywać odpowiednie operacje i zwracać dany parametr\
    #do funkcji przekazany jest okienkowany sygnał
    fprint.append(zero_crossing_rate(input_chunk=input_chunk))
    #jeśli zostanie podany argument -d, skrypt jest odpalony w trybie debugowania, więc wypisze wszystkie argumenty na ekran
    if args.debug:
        print(f"Zero_crossing_rate in fprint: {fprint[0]}\n\n")

    fprint.append(energy_spectral_denisity(input_chunk))
    if args.debug:
        print(f"Energy_spectral_denisity in fprint: {fprint[1]}\n\n")

    fprint.append(rms(input_chunk))
    if args.debug:
        print(f"Rms in fprint: {fprint[2]}\n\n")

    fprint.append(spectral_centroid(input_chunk))
    if args.debug:
        print(f"Spectral centroid in fprint: {fprint[3]}\n\n")

    fprint.append(octave_fft(input_chunk))
    if args.debug:
        print(f"octave_fft in fprint: {fprint[4]}\n\n")

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
