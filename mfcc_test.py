import numpy as np
import librosa
from support_functions.wave_open import wave_open
from support_functions.windowing import windowing
from scipy.signal import stft
'''
Parameters:	

y:np.ndarray [shape=(n,)] or None -> audio time series

sr:number > 0 [scalar] -> sampling rate of y

S:np.ndarray [shape=(d, t)] or None -> log-power Mel spectrogram

n_mfcc: int > 0 [scalar] -> number of MFCCs to return

dct_type:None, or {1, 2, 3} -> Discrete cosine transform (DCT) type. By default, DCT type-2 is used.

norm:None or ‘ortho’ -> If dct_type is 2 or 3, setting norm=’ortho’ uses an ortho-normal DCT basis. 
Normalization is not supported for dct_type=1.

kwargs:additional keyword arguments -> Arguments to melspectrogram, if operating on time series input

Returns:
	
M:np.ndarray [shape=(n_mfcc, t)] -> MFCC sequence
'''


def mfccs(left_channel, right_channel, sampling_rate, n_mfcc):

    ro_left = np.array([])
    ro_right = np.array([])

    for i in left_channel:
        ro_l = librosa.feature.mfcc(y=i, sr=sampling_rate, S=None, n_mfcc=n_mfcc, dct_type=2, norm='ortho')
        ro_left = np.append(ro_left,ro_l)

    if type(left_channel) == type(right_channel):
        for i in right_channel:
            ro_r = librosa.feature.mfcc(y=i, sr=sampling_rate, S=None, n_mfcc=n_mfcc, dct_type=2, norm='ortho')
            ro_right = np.append(ro_right, ro_r)
    else:
        ro_right = -1

    return ro_left, ro_right

data, number_of_frames, channels, sampling_rate, duration = wave_open(r'wav_samples\rock.wav', normalize=True, rm_constant=True)
freq_bin, time_bin, magnitudes = stft(data, fs=sampling_rate, window='hamming',
                                          nperseg=1024, noverlap=None)
left_channel, right_channel = windowing(data=data, sampling_rate=sampling_rate,
                                            channels=channels, window_size=2048, offset=0, to_mono=False,
                                            fill_zeros=True)
n_mfcc=12
a, b = mfccs(left_channel, right_channel, sampling_rate, n_mfcc)

print(a, b)

