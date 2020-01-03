import numpy as np
import scipy.io.wavfile as wav


class Sound:
    def __init__(self):
        rate, data = wav.read("input files/ma.wav")
        self.y = np.array(data)
        self.x = np.arange(len(data)) / float(rate)