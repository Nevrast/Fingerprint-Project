from skimage import util
from scipy.io import wavfile


sample_rate, wave_data = wavfile.read('sine_stereo_100.0.wav')
print(wave_data.shape)
wave_data_t = wave_data.T

print(wave_data_t[0::2].flatten().shape)
flat_L = wave_data_t[0::2].flatten()
flat_R = wave_data_t[1::2].flatten()

chunks_L = util.view_as_windows(flat_L, window_shape=(12,), step=12)
chunks_R = util.view_as_windows(flat_R, window_shape=(12,), step=8)
print(chunks_L)