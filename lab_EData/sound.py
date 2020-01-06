import numpy as np
import scipy.io.wavfile as wav


class Sound:
    def __init__(self, name_of_wav_file):
        rate, data = wav.read(name_of_wav_file)
        self.y = np.array(data)
        self.x = np.arange(len(data)) / float(rate)
        self.rate = rate
