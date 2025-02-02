from scipy.io.wavfile import write
import numpy as np

class Output:
    def __init__(self):
        return
    
    def __call__(self):
        return
    
    def write(self, Data, filename="AudiPy"):

        # sample rate
        SAMPLE_RATE = 44100                

        Transposed = Data.T

        write(filename + ".wav", SAMPLE_RATE, Transposed.astype(np.float32))