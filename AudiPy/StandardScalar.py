import numpy as np

class StandardScalar:
    def __init__(self):
        return

    def __call__(self):
        return
    
    # normalize data between the range of min to max with a sine curve
    def normalize_sine(self, data, minf, maxf):
        return ((maxf-minf) * np.abs(np.sin(data)) + minf)

    # normalize data between the range of min to max with a inverse function
    def normalize_inverse(self, data, minf, maxf):
        return ((maxf-minf) * data/max(data) + minf)

    # normalize to twelve tone
    def normalize_twelve_tone(self, data, minf=None, maxf=None):
        min_input = 12 * np.log2(minf / 63)
        max_input = 12 * np.log2(maxf / 63)

        data = np.subtract(data, np.min(data)) / np.subtract(np.max(data), np.min(data)) * (
        (max_input - min_input)) + min_input

        return np.multiply(63, np.power(2,np.divide(data,12)))

    # normalize to modal
    def normalize_modal(self, data, MODAL_VALUE, minf=None, maxf=None):
        min_input = 12 * np.log2(minf/63)
        max_input = 12 * np.log2(maxf/63)

        data  = np.subtract(data,np.min(data)) / np.subtract(np.max(data),np.min(data)) * (max_input-min_input) + min_input

        final = []
        for channel in data:
            channel_sine_wave = []
            for value in channel:
                quantized = int(value)
                if quantized % 12 in MODAL_VALUE:
                    sin_value = np.multiply(63, np.power(2,np.divide(quantized,12)))
                else:
                    quantized += 1
                    sin_value = np.multiply(63, np.power(2,np.divide(quantized,12)))
                channel_sine_wave.append(sin_value)
            final.append(channel_sine_wave)
        return final

    # normalize by scaled
    def normalize_scaled(self, data, minf, maxf):
        return np.subtract(data,np.min(data)) / np.subtract(np.max(data),np.min(data)) * ((maxf-minf)) + minf
