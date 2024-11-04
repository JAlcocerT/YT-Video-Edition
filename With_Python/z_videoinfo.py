import os
import subprocess
from pymediainfo import MediaInfo

# Define the directory where the videos are located
video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"

# Iterate through all MP4 files in the directory
for filename in os.listdir(video_directory):
    if filename.endswith(".MP4"):
        video_path = os.path.join(video_directory, filename)
        print(f"File: {filename}")

        # Get video information using pymediainfo
        media_info = MediaInfo.parse(video_path)
        for track in media_info.tracks:
            if track.track_type == "Video":
                rotation = track.rotation or "Not specified"
                width = track.width
                height = track.height
                codec = track.codec
                duration = track.duration / 1000  # Convert from milliseconds to seconds
                print(f"Rotation: {rotation}")
                print(f"Width: {width}")
                print(f"Height: {height}")
                print(f"Codec: {codec}")
                print(f"Duration: {duration:.2f} seconds")
                break  # Exit after processing the video track

        # Get additional information using ffprobe
        ffprobe_cmd = [
            "ffprobe",
            "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height,duration,codec_name,r_frame_rate",
            "-show_entries", "stream_tags=rotate",
            video_path
        ]
        
        ffprobe_output = subprocess.run(ffprobe_cmd, capture_output=True, text=True)
        print(ffprobe_output.stdout.strip())  # Print ffprobe output

        print("-----------------------")