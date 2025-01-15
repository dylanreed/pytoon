import os

file_path = "/Users/nervous/Documents/GitHub/pytoon/.test/speech.wav"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()
else:
    print("File is accessible.")
import nltk
nltk.download('averaged_perceptron_tagger')

from nltk.tag import PerceptronTagger
print(PerceptronTagger.LANG)  # Ensure it outputs "en"
