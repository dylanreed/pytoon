from pytoon.animator import animate
from moviepy import ImageClip
from pydub import AudioSegment
import torchaudio
import nltk
from nltk.tag import pos_tag, PerceptronTagger
from nltk.data import load

# Force use of "en" language
PerceptronTagger.LANG = "en"
nltk.data.path.append('/Users/nervous/nltk_data')

waveform, sample_rate = torchaudio.load("/Users/nervous/Documents/GitHub/pytoon/.test/speech.wav", backend="sox")

# Constants
FPS = 48
TEXT_PATH = "./.test/speech.txt"  # Path to a transcript text file (optional)
AUDIO_PATH = "./.test/speech.wav"  # Path to an audio file of speech
BACKGROUND_IMAGE = "./.test/image.png"  # Path to an image for the video background
OUTPUT_VIDEO_1 = "./output_animation_with_transcript.mp4"  # Output for Example 1
OUTPUT_VIDEO_2 = "./output_animation_auto_transcript.mp4"  # Output for Example 2

# Example 1: Providing a Transcript
# ---------------------------------
#print("Example 1: Using a provided transcript.")

# Load the transcript
#print("loading trascript")
#with open(TEXT_PATH, "r") as file:
#    transcript = file.read()

# Generate the animation with the provided transcript
#print("Generating animation with a provided transcript...")
#animation = animate(audio_file=AUDIO_PATH)

# Create a background clip
#print("background clip")
#background_clip = ImageClip(BACKGROUND_IMAGE)
#background_clip = background_clip.set_fps(FPS).set_duration(animation.duration)

# Export the animation
#print(f"Exporting animation to {OUTPUT_VIDEO_1}...")
#animation.export(path=OUTPUT_VIDEO_1, background=background_clip)
#print(f"Animation exported successfully to {OUTPUT_VIDEO_1}!")

# Example 2: Automatic Transcript Generation
# ------------------------------------------
print("\nExample 2: Automatically generating a transcript.")

#convert .mp3 to .wav
#audio = AudioSegment.from_file("/Users/nervous/Documents/GitHub/pytoon/.test/speech.mp3", format="mp3")
#udio.export("/Users/nervous/Documents/GitHub/pytoon/.test/speech.wav", format="wav")

# Generate the animation without providing a transcript
# PyToon will automatically generate the transcript using text-to-speech.
print("Generating animation with automatic transcript generation...")
animation = animate(audio_file=AUDIO_PATH)

# Create a background clip
background_clip = ImageClip(BACKGROUND_IMAGE)
background_clip = background_clip.set_fps(FPS).set_duration(animation.duration)

# Export the animation
print(f"Exporting animation to {OUTPUT_VIDEO_2}...")
animation.export(path=OUTPUT_VIDEO_2, background=background_clip)
print(f"Animation exported successfully to {OUTPUT_VIDEO_2}!")
