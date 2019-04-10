import wave
import numpy as np


def sine_generator(freq, duration=10.0, sample_rate=44100.0, stereo=True):
    amp = np.power(2, 16) / 2 - 1
    time = np.arange(0, duration, 1./sample_rate)
    sine_wave = amp * np.sin(freq * 2 * np.pi * time)
    sine_16bit = sine_wave.astype(np.int16)
    if stereo:
        stereo_sine = np.repeat(sine_16bit, 2)
        stereo_name = 'stereo_'
        wav_out = wave.open(r'sine_' + stereo_name + str(freq) + '_' + str(sample_rate/1000) + 'kHz.wav', 'wb')
        wav_out.setnchannels(2)
        wav_out.setsampwidth(2)
        wav_out.setframerate(sample_rate)
        wav_out.writeframes(stereo_sine)
    else:
        stereo_name = 'mono_'
        wav_out = wave.open(r'sine_' + stereo_name + str(freq) + '_' + str(sample_rate/1000) + 'kHz.wav', 'wb')
        wav_out.setnchannels(1)
        wav_out.setsampwidth(2)
        wav_out.setframerate(sample_rate)
        wav_out.writeframes(sine_16bit)
    wav_out.close()
