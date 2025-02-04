import numpy as np

class Generator:
    def __init__(self):
        return

    def __call__(self):
        return

    def data_matrix(self, array, time=10):
        SAMPLE_RATE = 44100 
        # calculate sample steps
        ns = np.linspace(0., time, SAMPLE_RATE * time)
        amplitude = 0.3

        # Apply fade-in and fade-out
        attack_time = 0.01  # 10ms fade-in
        decay_time = 0.01  # 10ms fade-out

        # samples per pitch
        sample_size = int(len(ns)/len(array[0]))

        converted_music = []

        for channel in array:
            previous_samples = 0
            new_channel = []

            for freq in channel:
                cur_samples = ns[previous_samples:(previous_samples + sample_size)]
                previous_samples += sample_size
                sine_wave = (amplitude * np.sin(2. * np.pi * freq * cur_samples) +
                             0.3 * (amplitude * np.sin(2. * np.pi * freq * cur_samples)) +
                             0.2 * (amplitude * np.sin(2. * np.pi * freq * cur_samples)))

                # Calculate Envelope
                attack_len = int(attack_time * freq)
                decay_len = int(decay_time * freq)

                envelope = np.ones_like(sine_wave)
                envelope[:attack_len] = np.linspace(0, 1, attack_len)
                envelope[-decay_len:] = np.linspace(1, 0, decay_len)

                new_channel.append(sine_wave * envelope)

            new_channel = np.concatenate(new_channel)
            converted_music.append(new_channel)

        # each row is a channel
        converted_music = np.vstack(converted_music)

        return converted_music
