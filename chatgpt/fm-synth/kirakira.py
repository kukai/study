import numpy as np
from scipy.io.wavfile import write

# Define the notes and their frequencies
notes = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00
}

# Kira Kira Hoshi melody and rhythm
melody = ['C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C']
rhythm = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2]

# Parameters for FM synthesis
A = 1.0  # amplitude
fm = 220.0  # modulator frequency (Hz)
I = 5.0  # modulation index
sampling_rate = 44100  # number of samples per second

# Define a function to generate FM synthesized sound for a given note and duration
def generate_note(note, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration))
    fc = notes[note]
    y = A * np.sin(2 * np.pi * fc * t + I * np.sin(2 * np.pi * fm * t))
    return y

# Create the melody using FM synthesis
sound = []
for i, note in enumerate(melody):
    sound.extend(generate_note(note, rhythm[i]))
sound = np.array(sound)

# Convert the signal to 16-bit PCM format for audio playback
sound = np.int16(sound * 32767)

# Save the synthesized melody as a WAV file
kira_kira_path = "./kira_kira_hoshi_fm.wav"
write(kira_kira_path, sampling_rate, sound)
