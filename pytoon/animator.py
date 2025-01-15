import json
from moviepy import ImageClip, CompositeVideoClip, AudioFileClip
from moviepy.video.VideoClip import VideoClip
import numpy as np
import random
import torchaudio


class Animate:
    def __init__(self, audio_file, phonemes=None, fps=48, viseme_file="/Users/nervous/Documents/GitHub/pytoon/pytoon/assets/visemes.json"):
        self.audio_file = audio_file
        self.fps = fps
        self.viseme_sequence = phonemes if phonemes else []
        self.viseme_duration = 1 / fps  # Duration of each viseme frame

        # Load viseme-to-image mapping from JSON
        with open(viseme_file, "r") as f:
            self.viseme_map = json.load(f)

    def normalize_phoneme(self, phoneme):
        """
        Normalize phonemes to match the keys in visemes.json.
        """
        return phoneme if phoneme in self.viseme_map else "PAUSE"

    def extract_phoneme_timestamps(self):
        """
        Simulate phoneme alignment with varying durations.
        Replace this with a real alignment tool like Gentle.
        """
        audio_info = torchaudio.info(self.audio_file)
        total_duration = audio_info.num_frames / audio_info.sample_rate
        num_phonemes = len(self.viseme_sequence)

        durations = [0.1 + 0.1 * (i % 5) for i in range(num_phonemes)]
        durations = [d / sum(durations) * total_duration for d in durations]

        start_times = [sum(durations[:i]) for i in range(num_phonemes)]
        end_times = [start + dur for start, dur in zip(start_times, durations)]

        return list(zip(start_times, end_times))

    def export_viseme_json(self, output_path):
        """
        Exports a JSON file containing visemes and their timestamps.
        """
        timestamps = self.extract_phoneme_timestamps()
        viseme_data = []

        for idx, (start_time, end_time) in enumerate(timestamps):
            phoneme = self.normalize_phoneme(self.viseme_sequence[idx])
            viseme = self.viseme_map.get(phoneme, "PAUSE")
            viseme_data.append({
                "phoneme": phoneme,
                "viseme": viseme,
                "start_time": round(start_time, 3),
                "end_time": round(end_time, 3)
            })

        with open(output_path, "w") as f:
            json.dump(viseme_data, f, indent=4)

        print(f"Viseme data exported to {output_path}")

    def compile_animation(self):
        """
        Generate the animation using timestamps from viseme_sequence.json.
        """
        # Create mouth shape clips
        mouth_clips = []
        for idx, item in enumerate(self.viseme_sequence):
            phoneme = item["phoneme"]  # Extract the phoneme
            start_time = item["start_time"]
            end_time = item["end_time"]

            # Normalize phoneme and get viseme
            normalized_phoneme = self.normalize_phoneme(phoneme)
            viseme_images = self.viseme_map.get(normalized_phoneme, ["mouth_closed.png"])  # Default to "mouth_closed.png"
            selected_image = random.choice(viseme_images)

            # Create mouth clip
            mouth_clip = (
                ImageClip(f"visemes/{selected_image}")
                .set_duration(end_time - start_time)
                .set_start(start_time)
                .set_position(("center", "center"))
            )
            mouth_clips.append(mouth_clip)

        # Create a black background (720p resolution)
        total_duration = self.viseme_sequence[-1]["end_time"]  # Duration equals the end time of the last viseme
        black_background = VideoClip(
            lambda t: np.zeros((720, 1280, 3), dtype=np.uint8), duration=total_duration
        )

        # Composite all clips with the black background
        final_clip = CompositeVideoClip([black_background] + mouth_clips)
        return final_clip



    def export(self, path):
        animation_clip = self.compile_animation()
        audio = AudioFileClip(self.audio_file)
        animation_with_audio = animation_clip.with_audio(audio)
        animation_with_audio.write_videofile(path, fps=self.fps)
