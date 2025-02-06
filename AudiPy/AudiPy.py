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

    def pre_process(self, filename, image_direction="Right"):
        matrix = self.input.take_file(filename, image_direction)
        return matrix
    
    def convert_to_audio(self, data, mode=None, min_freq=20, max_freq=4000, time=10,file_name="AudiPy"):
        if mode == "Ionian" or mode == "Major":
            MODAL_VALUE = [0, 2, 4, 5, 7, 9, 11]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Dorian":
            MODAL_VALUE = [0, 2, 3, 5, 7, 9, 11]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Phrygian":
            MODAL_VALUE = [0, 1, 3, 5, 7, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Lydian":
            MODAL_VALUE = [0, 2, 4, 6, 7, 9, 11]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Mixolydian":
            MODAL_VALUE = [0, 2, 4, 5, 7, 9, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Aeolian" or mode == "Minor":
            MODAL_VALUE = [0, 2, 3, 5, 7, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Locrian":
            MODAL_VALUE = [0, 1, 3, 4, 5, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        elif mode == "Whole Tone":
            MODAL_VALUE = [0, 2, 4, 6, 8, 10]
            matrix = self.scalar.normalize_modal(data, MODAL_VALUE, min_freq, max_freq)
        else:
            matrix = self.scalar.normalize_twelve_tone(data, min_freq, max_freq)
        
        normalized = self.generator.data_matrix(matrix, time)
        return self.output.write(normalized, file_name=file_name)
