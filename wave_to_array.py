from skimage import util
from scipy.io import wavfile
import numpy as np


def wave_to_array(file_name, window_size=2048, offset=0, to_mono=False):
    """
    :param file_name: string, name or path to the file
    :param window_size: int, size of single window
    :param offset: int, defines how many samples will overlap
    :param to_mono: bool, if True converts stereo file to mono
    :return: sample_rate, sampling frequency of wav file
    :return: windows_l, left channel signal or mono signal split into windows
    :return: windows_r, right channel signal split into windows
    """

# sprawdzanie czy offset jest potęgą dwójki i jest mniejszy niż rozmiar okna
    if not (offset == 0 or ((offset & (offset - 1)) == 0) and offset <= window_size):
        raise ValueError("Offset must be power of two and less than window size.")

# sprawdzanie czy rozmiar okienka jest potęgą dwójki
    if not (window_size != 0 and ((window_size & (window_size - 1)) == 0)):
        raise ValueError("Window size must be power of two.")

    sample_rate, wave_data = wavfile.read(file_name)  # wczytanie pliku
    wave_data_t = wave_data.T  # transponowanie macierzy
    offset = window_size - offset  # obliczanie nakładania się okienek

# jeśli nie chcemy offsetu to krok musi być równy długości okna
    if offset == 0:
        offset = window_size

# jeśli chcemy sygnał stereo zmienić na mono to trzeba zsumować próbki i policzyć średnią z kanałó
    if wave_data_t.ndim == 2 and to_mono:
        wave_data_t = (wave_data_t.sum(axis=0)/2).astype(np.int16)

# obsługa plików jednokanałowych
    if wave_data_t.ndim == 1:
        windows_l = util.view_as_windows(wave_data_t, window_shape=(window_size,), step=offset)
        windows_r = None

# obsługa plików dwukanałowych
    elif wave_data_t.ndim == 2:
        flat_l = wave_data_t[0::2].flatten()  # ektrakcja kanału lewego i 'spłaszczenie' go do jednego wymiaru
        flat_r = wave_data_t[1::2].flatten()  # to samo dla kanału prawego(lewy to próbki parzyste, a prawy nieparzyste)
        windows_l = util.view_as_windows(flat_l, window_shape=(window_size,), step=offset)
        windows_r = util.view_as_windows(flat_r, window_shape=(window_size,), step=offset)

# większa ilość kanałów nie jest narazie obsługiwana
    else:
        raise ValueError("Unsupported shape of wave file.")

    return sample_rate, windows_l, windows_r
