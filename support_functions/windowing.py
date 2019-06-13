import numpy as np


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

    step = window_size - offset
    if fill_zeros and sampling_rate % window_size != 0:
        nadd = (-(data.shape[-1] - window_size) % step) % window_size
        zeros_shape = list(data.shape[:-1]) + [nadd]
        data = np.concatenate((data, np.zeros(zeros_shape)), axis=-1)
    shape = data.shape[:-1] + ((data.shape[-1] - offset) // step, window_size)
    strides = data.strides[:-1] + (step * data.strides[-1], data.strides[-1])

    if data.ndim == 1:
        windows_l = np.lib.stride_tricks.as_strided(data, shape=shape, strides=strides)
        windows_r = None

    elif data.ndim == 2:
        windows = np.lib.stride_tricks.as_strided(data, shape=shape, strides=strides)
        windows_l = windows[0]
        windows_r = windows[1]

    # większa ilość kanałów nie jest narazie obsługiwana
    else:
        raise ValueError("Unsupported shape of wave file.")

    time = np.arange(window_size / 2, data.shape[-1] - window_size / 2 + 1,
                     window_size - offset) / float(sampling_rate)

    return windows_l, windows_r, time
