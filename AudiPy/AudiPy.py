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
    
    def convert_to_audio(self, data, mode, min_freq, max_freq, time):
        if mode == "Ionian" or mode == "Major":
            MODAL_VALUE = [0, 2, 4, 5, 7, 9, 11]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Dorian":
            MODAL_VALUE = [0, 2, 3, 5, 7, 9, 11]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Phrygian":
            MODAL_VALUE = [0, 1, 3, 5, 7, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Lydian":
            MODAL_VALUE = [0, 2, 4, 6, 7, 9, 11]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Mixolydian":
            MODAL_VALUE = [0, 2, 4, 5, 7, 9, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Aeolian" or mode == "Minor":
            MODAL_VALUE = [0, 2, 3, 5, 7, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Locrian":
            MODAL_VALUE = [0, 1, 3, 4, 5, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        if mode == "Whole Tone":
            MODAL_VALUE = [0, 2, 4, 6, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        else:
            matrix = self.scalar.normalize_twelve_tone(data, min_freq, max_freq)
            
        wave = self.generator.data_matrix(matrix, time)
        return self.output.write(wave)
