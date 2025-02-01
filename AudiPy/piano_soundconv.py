import numpy as np

def apply_adsr(wave, sample_rate, attack=0.05, decay=0.1, sustain_level=0.7, sustain_time=0.3, release=0.2):
    """Applies ADSR envelope to a waveform."""
    total_samples = len(wave)
    
    # Convert time values to sample indices
    attack_samples = int(sample_rate * attack)
    decay_samples = int(sample_rate * decay)
    sustain_samples = int(sample_rate * sustain_time)
    release_samples = int(sample_rate * release)

    # Ensure total samples do not exceed the waveform length
    sustain_samples = max(0, total_samples - (attack_samples + decay_samples + release_samples))

    # Attack phase: Linearly increase amplitude
    attack_env = np.linspace(0, 1, attack_samples)

    # Decay phase: Drop to sustain level
    decay_env = np.linspace(1, sustain_level, decay_samples)

    # Sustain phase: Hold the sustain level
    sustain_env = np.ones(sustain_samples) * sustain_level

    # Release phase: Gradually drop to zero
    release_env = np.linspace(sustain_level, 0, release_samples)

    # Concatenate all envelope parts
    envelope = np.concatenate([attack_env, decay_env, sustain_env, release_env])

    # Ensure the envelope matches the wave size
    envelope = np.pad(envelope, (0, max(0, total_samples - len(envelope))), mode='constant')

    return (wave * envelope)

def add_harmonics(base_wave, freq, sample_rate, harmonics=[(2, 0.5), (3, 0.3), (4, 0.2)]):
    """
    Adds harmonic overtones to a given waveform.
    harmonics = [(multiple, amplitude_factor), ...]
    """
    harmonic_wave = np.copy(base_wave)
    
    for multiple, amplitude_factor in harmonics:
        harmonic_wave += amplitude_factor * np.sin(2. * np.pi * freq * multiple * np.linspace(0., len(base_wave)/sample_rate, len(base_wave)))
    
    return harmonic_wave / (1 + sum(a for _, a in harmonics))  # Normalize to avoid clipping