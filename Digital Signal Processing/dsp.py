import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import scipy.signal
import contextlib

inputFileName = "soundIn.wav"
outputFileName = "soundOut.wav"

n = round(23+4) # 23 April
k = 1232
l = 2 # 2. BOGDAN BERNOVICI

# functia care returneaza canalele
def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8
    elif sample_width == 2:
        dtype = np.int16
    else:
        raise ValueError("Suporta doar wav de 8 sau 16 bits.")

    channels = np.fromstring(raw_bytes, dtype=dtype)

    if interleaved:
        # daca canalele sunt intercalate
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # daca nu sunt intercalate
        channels.shape = (n_channels, n_frames)

    return channels


with contextlib.closing(wave.open(inputFileName,'rb')) as spf:
    fs = spf.getframerate() #sample rate
    ampWidth = spf.getsampwidth()
    nChannels = spf.getnchannels()
    nFrames = spf.getnframes()

    # extrag raw audio din wav-ul multi-channel
    signal = spf.readframes(nFrames * nChannels)
    signalDecoded = np.fromstring(signal, 'Int16')
    spf.close()
    channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

    # Plotul semnalului original
    Time = np.linspace(0, len(signalDecoded) / fs, num=len(signalDecoded))

    # Adaugarea filtrului butter
    b,a = scipy.signal.butter(l % 4, 0.5, 'low')
    filtered_butter_signal = scipy.signal.filtfilt(b, a, signalDecoded)
    filtered = filtered_butter_signal.astype(channels.dtype)
    FilteredTime = np.linspace(0, len(filtered_butter_signal) / fs, num=len(filtered_butter_signal))

    wav_file = wave.open(outputFileName, "w")
    wav_file.setparams((1, ampWidth, fs, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()

    # Plotul inainte de filtrare
    plt.figure(1)
    plt.title('Signal Wave')
    plt.plot(Time,signalDecoded)
    plt.show()

    # Plotul dupa filtrare
    plt.figure(2)
    plt.title('Filtered Wave with Butter')
    plt.plot(FilteredTime, filtered_butter_signal)
    plt.show()

