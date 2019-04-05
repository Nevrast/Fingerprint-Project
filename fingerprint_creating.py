
from sys import argv

#import potrzebnych funkcji
from wave_to_list import wave_to_list
from zero_crossing_rate import zero_crossing_rate
from energy_spectral_density import energy_spectral_denisity
from rms import rms
from spectral_centroid import spectral_centroid
from oct import octave_fft

#przypisanie argumentów z cmd do zmiennych
#żeby wywołać skrypt dla sygnału "test.wav" i zapisać f-print do pliku test.txt znajdującego się w tym samym katalogu, odpal skrypt poleceniem: python fingerprint_creating.py ./test.wav ./test.txt
#później dodam flagi -i, -o, ewentualnie -d do debugowania
INPUT_PATH, OUTPUT_PATH = argv[1], argv[2]
print (f"Input file: {INPUT_PATH}")
print (f"Output file: {OUTPUT_PATH}")

def fing_creat(input):
    #wczytywanie pliku
    #input_chunk to zokienkowany sygnał?
    input_signal, input_chunk, sampling_rate = wave_to_list(input, window_size=2048)

    #to jest lista, która stanie się fingerprintem
    fprint = []

    # dodawanie kolejnych parametrów do listy
    # nazwy funkcji powinny być nazwą parametru
    # każda funkcja powinna przyjmować jako argument listę, która zawiera zokienkowany sygnał wejściowy,\
    # następnie wykonywać odpowiednie operacje i zwracać dany parametr\

    fprint.append(zero_crossing_rate(input_chunk=input_chunk))
    #na razie będę wyświetlać zawartość fingerprinta po każdej funkcji, później postaram się to przenieść do trybu debugowania
    #print(f"Zero_crossing_rate in fprint: {fprint[0]}\n\n")

    fprint.append(energy_spectral_denisity(input_chunk))
    #print(f"Energy_spectral_denisity in fprint: {fprint[1]}\n\n")

    fprint.append(rms(input_chunk))
    #print(f"Rms in fprint: {fprint[2]}\n\n")

    fprint.append(spectral_centroid(input_chunk))
    #print(f"Spectral centroid in fprint: {fprint[3]}\n\n")

    fprint.append(octave_fft(input_chunk))
    print(f"octave_fft in fprint: {fprint[4]}\n\n")

    return fprint

def fing_save(fingerprint, output):
    #tu będzie operacja zapisania do pliku jeśli ścieżka została podana
    file = open(output, 'w')
    for elem in fingerprint:
        file.write(str(elem))
    file.close()

#wywołanie funkcji
new_fingerprint = fing_creat(INPUT_PATH)
#if #został podany argument -o :
fing_save(new_fingerprint, OUTPUT_PATH)
