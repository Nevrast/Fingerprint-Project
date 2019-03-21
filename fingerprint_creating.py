from sys import argv

#import potrzebnych funkcji
from zero_crossing_rate import zero_crossing_rate
from wave_to_list import wave_to_list

#przypisanie argumentów z cmd do zmiennych
#żeby wywołać skrypt dla sygnału "test.wav" i zapisać f-print do pliku test.txt znajdującego się w tym samym katalogu, odpal skrypt poleceniem: python fingerprint_creating.py ./test.wav ./test.txt
#później dodam flagi -i, -o, ewentualnie -d do debugowania
INPUT_PATH, OUTPUT_PATH = argv[1], argv[2]
print (f"Input file: {INPUT_PATH}")
print (f"Output file: {OUTPUT_PATH}")

def fing_creat(input):
    #wczytywanie pliku
    input_signal, input_chunk = wave_to_list(input)
    # ...

    #to jest lista, która stanie się fingerprintem
    fprint = []

    # dodawanie kolejnych parametrów do listy
    #nazwy funkcji powinny być nazwą parametru
    #każda funkcja powinna przyjmować jako argument istniejącą już listę fprint i sygnał wejściowy
    # \(przetworzony już wcześniej na dane cyfrowe), następnie wykonywać odpowiednie operacje, aby uzyskać dany parametr\
    #funkcją append dodać parametr jako kolejny element listy i zwracać listę, która była argumentem

    zero_crossing_rate(fingerprint, input_signal)
    #na razie będę wyświetlać zawartość fingerprinta po każdej funkcji, później postaram się to przenieść do trybu debugowania
    print(f"Fingerpint after zero_crossing_rate: {fprint}\n\n")
    #tu miejsce też na pozostałe funkcje

    return fprint

def fing_save(fingerprint, output):
    #tu będzie operacja zapisania do pliku jeśli ścieżka została podana
    pass

#wywołanie funkcji
new_fingerprint = fing_creat(INPUT_PATH)
#if #został podany argument -o :
fing_save(new_fingerprint, OUTPUT_PATH)
