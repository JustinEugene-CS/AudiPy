from .StandardScalar import StandardScalar
from .Generator import Generator
from .Output import Output
from .Input import Input

class AudiPy():

    def __init__(self):
        self.scalar = StandardScalar()
        self.generator = Generator()
        self.output = Output()
        self.input = Input()
        return
    
    def __call__(self):
        return

    def pre_process(self, filename):
        matrix = self.input.take_file(filename)
        return matrix
    
    def convert_to_audio(self, data, min_freq, max_freq, time, modal, ascending = None):
        if modal:
            matrix = self.scalar.normalize_modal(data, min_freq, max_freq)
        else:
            matrix = self.scalar.normalize_twelve_tone(data, min_freq, max_freq)
            
        wave = self.generator.data_matrix(matrix, time)
        return self.output.write(wave)
