import wave_to_list
import numpy as np

wave, chunk, framerate = wave_to_list.wave_to_list('ChillingMusic.wav')
def stft_bins(wave, chunk, d=1.0):
    wave = np.array(wave)
    l = len(chunk)
    Nwindows = wave.size // l
    t = np.arange(Nwindows) * (l * d)
    f = np.fft.rfftfreq(l, d)
    return t, f
print ( stft_bins(wave, chunk))

"""
        Short-time Fourier transform: convert a 1D vector to a 2D array
        The short-time Fourier transform (STFT) breaks a long vector into disjoint
        chunks (no overlap) and runs an FFT (Fast Fourier Transform) on each chunk.
        The resulting 2D array can 
        Parameters
        ----------
        x : array_like
            Input signal (expected to be real)
        Nwin : int
            Length of each window (chunk of the signal). Should be ≪ `len(x)`.
        -------
        out : complex ndarray
            `len(x) // Nwin` by `Nfft` complex array representing the STFT of `x`.
"""