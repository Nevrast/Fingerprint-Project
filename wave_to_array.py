from skimage import util
from scipy.io import wavfile
import numpy as np

sample_rate, wave_data = wavfile.read('sine_stereo_100.0.wav')
print(wave_data.shape)
wave_data_T = wave_data.T

print(wave_data_T[0::2].flatten().shape)
#print(wave_data_T)



chunks = util.view_as_windows(wave_data_T.flatten(), window_shape=(1024,), step=int(sample_rate/2))

print(chunks.shape)