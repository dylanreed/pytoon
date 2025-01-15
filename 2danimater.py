from pytoon.animator import Animate

# Constants
FPS = 48
AUDIO_PATH = "/Users/nervous/Documents/GitHub/pytoon/.test/inputs/audio.wav"  # Path to the audio file of speech
VISEME_SEQUENCE_FILE = "/Users/nervous/Documents/GitHub/pytoon/output/viseme_sequence.json"  # Path to viseme sequence JSON
OUTPUT_VIDEO = "/Users/nervous/Documents/GitHub/pytoon/output/mouth.mp4"  # Path for animation

# Load viseme sequence from JSON file
def load_viseme_sequence(file_path):
    import json
    with open(file_path, "r") as file:
        return json.load(file)

# Load the viseme sequence
print(f"Loading viseme sequence from {VISEME_SEQUENCE_FILE}...")
viseme_sequence = load_viseme_sequence(VISEME_SEQUENCE_FILE)
print(f"Loaded viseme sequence: {viseme_sequence}")

# Extract phonemes from the viseme sequence
phoneme_sequence = [item["phoneme"] for item in viseme_sequence]
print(f"Extracted phoneme sequence: {phoneme_sequence}")

# Generate animation
animation = Animate(audio_file=AUDIO_PATH, phonemes=phoneme_sequence, fps=FPS)

# Export the animation video
print(f"Exporting animation to {OUTPUT_VIDEO}...")
animation.export(path=OUTPUT_VIDEO)
print(f"Animation exported successfully to {OUTPUT_VIDEO}!")
