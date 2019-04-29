import numpy as np

def stft_bins(input_signal, input_chunk, d=1.0):
    input_signal = np.array(input_signal)
    lic = len(input_chunk)
    Nwindows = input_signal.size // lic
    t = np.arange(Nwindows) * (lic * d)
    f = np.fft.rfftfreq(lic, d)
    return t, f
print ( stft_bins(input_signal, input_chunk))

"""
        Short-time Fourier transform: convert a 1D vector to a 2D array
        The short-time Fourier transform (STFT) breaks a long vector into disjoint
        chunks (no overlap) and runs an FFT (Fast Fourier Transform) on each chunk.
        The resulting 2D array can 
        Parameters
        ----------
        input_signal : array_like
            Input signal (expected to be real)
        input_chunk: int
            Length of each window (chunk of the signal). Should be ≪ `len(input_signal)`.
        -------
        out : complex ndarray
            `len(input_signal) // input_chunk` by `Nfft` complex array representing the STFT of `input_signal`.
"""