import json
from phonemizer import phonemize  # Install with `pip install phonemizer`
from pydub import AudioSegment  # Install with `pip install pydub`

def load_phoneme_viseme_map():
    """Defines a mapping of phonemes to visemes (mouth shapes)."""
    return {
    "A": ["1.png"],
    "æ": ["1.png"],
    "ɑ:": ["1.png"],
    "ʌ": ["1.png"],
    "ɔ:": ["2"],
    "e": ["2"],
    "ɛ": ["2"],
    "ə": ["2"],
    "ɜ:": ["2"],
    "i:": ["7.png"],
    "ɪ": ["7.png"],
    "oʊ": ["10.png"],
    "əʊ": ["10.png"],
    "ɔɪ": ["10.png"],
    "u:": ["11.png"],
    "ʊ": ["11.png"],
    "eɪ": ["9.png"],
    "aɪ": ["9.png"],
    "aʊ": ["9.png"],
    "ɪə": ["9.png"],
    "eə": ["9.png"],
    "ʊə": ["9.png"],
    "p": ["9.png"],
    "b": ["9.png"],
    "m": ["9.png"],
    "f": ["8.png"],
    "v": ["8.png"],
    "t": ["7.png"],
    "d": ["7.png"],
    "s": ["7.png"],
    "z": ["7.png"],
    "ʃ": ["11.png"],
    "ʒ": ["11.png"],
    "ʧ": ["11.png"],
    "ʤ": ["11.png"],
    "k": ["11.png"],
    "g": ["11.png"],
    "ŋ": ["11.png"],
    "n": ["8.png"],
    "l": ["8.png"],
    "r": ["10.png"],
    "w": ["10.png"],
    "j": ["7.png"],
    "h": ["11.png"],
    "θ": ["7.png"],
    "ð": ["7.png"],
    "PAUSE": ["9.png"]
}


def read_transcript(file_path):
    """Reads the transcript text from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def get_audio_duration(audio_file):
    """Gets the duration of the audio file in milliseconds."""
    audio = AudioSegment.from_file(audio_file)
    return len(audio)

def map_phonemes_to_visemes_with_timing(transcript, audio_duration):
    """Converts transcript into a list of visemes with timing."""
    phoneme_viseme_map = load_phoneme_viseme_map()

    # Phonemize the transcript
    phonemes = phonemize(transcript, language="en-us", backend="espeak", strip=True)

    # Placeholder: Evenly distribute phonemes over the audio duration
    viseme_list = []
    phoneme_count = len(phonemes)
    time_per_phoneme = audio_duration / phoneme_count if phoneme_count else 0

    current_time = 0
    for phoneme in phonemes:
        viseme = phoneme_viseme_map.get(phoneme, "neutral")  # Default to 'neutral'
        viseme_list.append({
            "phoneme": viseme,
            "start_time": current_time,
            "end_time": current_time + time_per_phoneme
        })
        current_time += time_per_phoneme

    return viseme_list

# Example usage
if __name__ == "__main__":
    # File paths
    transcript_file = "/Users/nervous/Documents/GitHub/pytoon/.test/inputs/transcript.txt"
    audio_file = "/Users/nervous/Documents/GitHub/pytoon/.test/inputs/audio.wav"

    # Read transcript from the file
    transcript = read_transcript(transcript_file)

    if transcript:
        # Get audio duration
        audio_duration = get_audio_duration(audio_file)

        # Process the transcript to assign visemes with timing
        visemes = map_phonemes_to_visemes_with_timing(transcript, audio_duration)

        # Output viseme sequence with timing
        json_object = json.dumps(visemes, indent=4)
        with open("/Users/nervous/Documents/GitHub/pytoon/output/viseme_sequence.json", "w") as outfile:
            outfile.write(json_object)
        #print(json.dumps(visemes, indent=2))
