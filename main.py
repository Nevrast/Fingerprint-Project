import wave, struct, math

czestoscProbkowania = 44100.0
czasTrwania = 10.0
czestotliwosc = 440.0

wavef = wave.open('sinus_440.wav', 'w')
wavef.setnchannels(1)  # mono
wavef.setsampwidth(2)
wavef.setframerate(czestoscProbkowania)

for i in range(int(czasTrwania * czestoscProbkowania)):
    value = int(32767.0*math.sin(czestotliwosc*2.0*math.pi*float(i)/float(czestoscProbkowania)))
    data = struct.pack('<h', value)
    print(data)
    wavef.writeframesraw(data)

wavef.close()