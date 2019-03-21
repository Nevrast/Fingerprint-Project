test
from sys import argv

#do odkomentowania
#from zero_crossing_rate import zero_crossing_rate

#przypisanie argumentów z cmd do zmiennych
#żeby wywołać skrypt dla sygnału "test.wav" znajdującego się w tym samym katalogu, odpal skrypt poleceniem: python fingerprint_creating.py ./test.wav
#później dodam flagi -i, -o, ewentualnie -d do debugowania
INPUT_PATH, OUTPUT_PATH = argv[1], argv[2]

def fing_creat(input):
    #tu będzie jakieś wczytywanie
    #input_signal=
    # ...
    fingerprint = []


    # dodawanie kolejnych parametrów, nazwy funkcji powinny być nazwą parametru
    #każda funkcja powinna przyjmować jako argument istniejącą już listę i sygnał wejściowy
    # \(wyżej przetworzony już na dane cyfrowe), następnie wykonywać odpowiednie operacje, aby uzyskać dany parametr\
    #funkcją append dodać parametr jako kolejny element listy i zwracać listę, która była argumentem

    zero_crossing_rate(fingerprint, input_signal)
    #na razie będę wyświetlać zawartość fingerprinta po każdej funkcji, później postaram się to przenieść do trybu debugowania
    print(f"Fingerpint after zero_crossing_rate: {fingerprint}\n\n")
    #tu miejsce też na pozostałe funkcje

    return fingerprint

def fing_save(fingerprint, output):
    #tu będzie operacja zapisania do pliku jeśli ścieżka została podana
    pass

#wywołanie funkcji
fing_creat(INPUT_PATH)
#if #został podany argument -o :
fing_save(fingerprint, OUTPUT_PATH)
