import numpy as np
import librosa


def spectral_centroid(input_chunk, samplerate=44100):
    """
    :param input_chunk: list2D, waveform split into chunks
    :param samplerate: int, samplerate of signal
    :return: array of lists with spectral centroids over time
    """
    param = []
    for i in range(len(input_chunk)):
        sc = librosa.feature.spectral_centroid(np.array(input_chunk[i]), sr=samplerate)
        sc = sc.tolist()
        param.append(sc[0])
    return np.array(param)
