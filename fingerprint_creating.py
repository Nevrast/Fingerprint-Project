#moduł potrzebny do obsługi linii poleceń
import argparse


#import potrzebnych funkcji
from support_functions.wave_open import wave_open
from support_functions.windowing import windowing

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

from parameters.zcr import zero_crossing, zero_crossing_debug
#from parameters.energy_spectral_density import energy_spectral_denisity
from parameters.power_spectral_density import power_spectral_density, power_spectral_debug
from parameters.spectral_flatness import spectral_flatness, spectral_flatness_debug
from parameters.spectral_centroid import spectral_centroid, spectral_centroid_debug
from parameters.rms import rms, rms_debug
from parameters.spectral_roll_off import roll_off, roll_off_debug
# gdy chcemy pokazać wszystkie dane macierzy numpy należy odkomentować poniższe dwie linijki
# import sys
# np.set_printoptions(threshold=sys.maxsize)

# opis skryptu
parser = argparse.ArgumentParser(description='This is a script which creates fingerprint matrix for specified input signal.')
# obowiązkowy argument dla wejściowego pliku
parser.add_argument("input", help="- input signal")
# opcjonalny argument dla pliku wyjściowego
parser.add_argument("-o", "--output", help="- output file")
# aby wywołać tryb debugujący należy wywołać tylko flagę -d bez żadnej wartości
parser.add_argument("-d", "--debug", help="- debugging mode, this argument is called without any value",
                    default=False, action='store_true')

# rozpakowanie parsera
args = parser.parse_args()
# wyświetla nazwy plików wejściowego i wyjściowego tylko w trybie debug
if args.debug:
    print("Input file: ", args.input, "\n")
INPUT_PATH = args.input

if args.output:
    if args.debug:
        print("Output file:", args.output)
    OUTPUT_PATH = args.output


def fing_creat(input):
    # wczytywanie pliku

    window_size = 1024
    offset = 512
    data, number_of_frames, channels, sampling_rate, duration = wave_open(INPUT_PATH, normalize=True, rm_constant=True)
    left_channel, right_channel, w_time_bin = windowing(data=data, sampling_rate=sampling_rate, channels=channels,
                                                        window_size=window_size, offset=offset, to_mono=False,
                                                        fill_zeros=True)

    # freq_bin to częstotliwości odpowiadające amplitudom w każdym oknie czasowym
    # time_bin to czasowe pozycje kolejnych okienek
    # magnitudes to trójwymiarowa macierz zawierająca dwa kanały, z których każdy składa się z N liczby
    # okien czasowych, gdzie każde okno czasowe to wektor amplitud kolejnych częstotliwośći

    freq_bin, time_bin, magnitudes = stft(x=data, fs=sampling_rate, window='hann',
                                          nperseg=window_size, noverlap=offset, boundary=None)

    # to jest lista, do której zapisywane będą wszystkie parametry
    fprint = []

    # dodawanie kolejnych parametrów do listy
    # nazwy funkcji powinny być nazwą parametru
    # każda funkcja powinna przyjmować jako argument listę, która zawiera zokienkowany sygnał wejściowy,\
    # następnie wykonywać odpowiednie operacje i zwracać dany parametr\
    # do funkcji przekazany jest okienkowany sygnał
    zc_left, zc_right = zero_crossing(ch_left=left_channel, ch_right=right_channel)
    fprint.append(np.array([zc_left, zc_right]))
    # jeśli zostanie podany argument -d, skrypt jest odpalony w trybie debugowania,
    # więc wypisze wszystkie argumenty na ekran
    if args.debug:
        print(f"Zero_crossing_rate in fprint: {fprint[0]}\n\n")
        #pg-debug-plots
        zero_crossing_debug(zc_left=zc_left, zc_right=zc_right, time_bin=w_time_bin, duration=duration,
                            sampling_rate=sampling_rate, data=data)

    psd_left, psd_right = power_spectral_density(left_channel, right_channel, sampling_rate, "hann")
    fprint.append(np.array([psd_left, psd_right]))
    if args.debug:
        print(f"Power spectral denisity in fprint: {fprint[1]}\n\n")
        #power_spectra_debug()


    sc_left, sc_right = spectral_centroid(magnitudes=magnitudes, freq_bin=freq_bin)
    fprint.append(np.array([sc_left, sc_right]))
    if args.debug:
        print(f"Spectral centroid in fprint: {fprint[2]}\n\n")
        spectral_centroid_debug(sc_left=sc_left, sc_right=sc_right, sampling_rate=sampling_rate, duration=duration,
                                data=data, time_bin=time_bin)

    sf_left, sf_right = spectral_flatness(magnitudes=magnitudes)
    fprint.append(np.array([sf_left, sf_right]))
    if args.debug:
        print(f"Spectral flatness in fprint: {fprint[3]}\n\n")
        spectral_flatness_debug(sf_left=sf_left, sf_right=sf_right, time_bin=time_bin, duration=duration,
                                sampling_rate=sampling_rate, data=data)

    rms_left, rms_right = rms(left_channel=left_channel, right_channel=right_channel)
    fprint.append(np.array([rms_left, rms_right]))
    if args.debug:
        print(f'RMS in fprint: {fprint[4]}\n\n')
        rms_debug(rms_left=rms_left, rms_right=rms_right, time_bin=w_time_bin, duration=duration,
                  sampling_rate=sampling_rate, data=data)

    ro_left, ro_right = roll_off(magnitudes=magnitudes)
    fprint.append(np.array([ro_left, ro_right]))
    if args.debug:
        print(f'Spectral roll off in fprint: {fprint[5]}\n\n')
        roll_off_debug(ro_left=ro_left, ro_right=ro_right, time_bin=time_bin, duration=duration,
                       sampling_rate=sampling_rate, data=data)
    # jeśli jesteśmy w trybie -d trzeba wyświetlić też wykresy, plt.show() powinien być wywoływany tylko raz
    # dlatego znajduje się tutaj po więcej informacji polecam https://matplotlib.org/faq/howto_faq.html#use-show
    if args.debug:
        plt.show()
    # zwraca naszą listę
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
