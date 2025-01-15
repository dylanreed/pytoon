def viseme_sequencer(audio_file, fps, phonemes=None):
    """Generates viseme sequence based on phoneme input"""
    if phonemes:
        # Directly use precomputed phonemes
        print(f"Using provided phoneme sequence: {phonemes}")
        return phonemes
    else:
        raise ValueError("No phoneme sequence provided and forcealign is disabled.")
