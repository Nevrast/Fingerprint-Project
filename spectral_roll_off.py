import librosa

def spectral_roll_off(file_name):
    y, sr = librosa.load(file_name, sr=44100)
    S, phase = librosa.magphase(librosa.stft(y))
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    return rolloff, S

# --------------------- TESTS ------------------------
#print(spectral_roll_off('ChillingMusic.wav'))

#import matplotlib.pyplot as plt
#import numpy as np
#import librosa.display

#rolloff, S = spectral_roll_off('ChillingMusic.wav')
#plt.figure()
#plt.subplot(2, 1, 1)
#plt.semilogy(rolloff.T, label='Roll-off frequency')
#plt.ylabel('Hz')
#plt.xticks([])
#plt.xlim([0, rolloff.shape[-1]])
#plt.legend()
#plt.subplot(2, 1, 2)
#librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),y_axis='log', x_axis='time')
#plt.title('log Power spectrogram')
#plt.tight_layout()
#plt.show()



