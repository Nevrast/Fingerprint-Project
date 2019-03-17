#czytanie argumentów z command line'a, -i jako sygnał wejściowy i opcjonalnie -o jako lokalizacja do zapisania fingerprinta
from sys import argv

#przypisanie argumentów z cmd do zmiennych
INPUT_PATH, OUTPUT_PATH= argv

def fing_creat(input):
    #tu będzie jakieś wczytywanie
    #INPUT_SIGNAL =
    # ...

    fingerprint = []


    # dodawanie kolejnych parametrów, nazwy funkcji powinny być nazwą parametru
    #każda funkcja powinna przyjmować jako argument istniejącą już listę i sygnał wejściowy
    # \(wyżej przetworzony już na dane cyfrowe), następnie wykonywać odpowiednie operacje, aby uzyskać dany parametr\
    #funkcją append dodać parametr jako kolejny element listy i zwracać listę, która była argumentem
    function1(fingerprint, INPUT_SIGNAL)
    function2(fingerprint, INPUT_SIGNAL)
    function3(fingerprint, INPUT_SIGNAL)
    function4(fingerprint, INPUT_SIGNAL)

    return fingerprint

def fing_save(fingerprint, output):
    #tu będzie operacja zapisania do pliku jeśli ścieżka została podana
    pass

fing_creat(INPUT_PATH)

if #został podany argument -o :
    fing_save(fingerprint, OUTPUT_PATH)