import numpy as np
from skimage import util


def windowing(data, sampling_rate, channels, window_size=2048, offset=0, to_mono=False, fill_zeros=True):
    if not (offset == 0 or ((offset & (offset - 1)) == 0) and offset <= window_size):
        raise ValueError("Offset must be power of two and less than window size.")

    # sprawdzanie czy rozmiar okienka jest potęgą dwójki
    if not (window_size != 0 and ((window_size & (window_size - 1)) == 0)):
        raise ValueError("Window size must be power of two.")
    # print(data.shape)
    if data.ndim == 2 and to_mono:
        data = (data.sum(axis=0)/2).astype(np.int16)

    # if fill_zeros and sampling_rate % window_size != 0:
    #     zeros = np.zeros((channels, window_size - (data.shape[1] % window_size)),dtype=np.int16)
    #     data = np.append(data, zeros, axis=1)

    offset = window_size - offset

    if data.ndim == 1:
        if fill_zeros and sampling_rate % window_size != 0:
            zeros = np.zeros((channels, window_size - (data.shape[0] % window_size)),
                             dtype=np.int16)
            data = np.append(data, zeros)
        windows_l = util.view_as_windows(data,
                                         window_shape=(window_size,), step=offset)
        windows_r = None

    elif data.ndim == 2:
        if fill_zeros and sampling_rate % window_size != 0:
            zeros = np.zeros((channels, window_size - (data.shape[1] % window_size)),
                             dtype=np.int16)
            data = np.append(data, zeros, axis=1)
        windows_l = util.view_as_windows(data[0],
                                         window_shape=(window_size,), step=offset)
        windows_r = util.view_as_windows(data[1],
                                         window_shape=(window_size,), step=offset)

# większa ilość kanałów nie jest narazie obsługiwana
    else:
        raise ValueError("Unsupported shape of wave file.")
    return windows_l, windows_r
