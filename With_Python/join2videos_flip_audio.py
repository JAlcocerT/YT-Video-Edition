# ### python3 join2videos_flip.py

import os
from pymediainfo import MediaInfo
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

# Define the directory where the videos are located
video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"
audio_file = os.path.join(video_directory, "audio.mp3")  # The .mp3 file in the same folder

# Initialize a list to store video information
video_info = []
video_files = []

# Gather video information and check properties
for filename in os.listdir(video_directory):
    if filename.endswith(".MP4"):
        video_path = os.path.join(video_directory, filename)
        media_info = MediaInfo.parse(video_path)

        for track in media_info.tracks:
            if track.track_type == "Video":
                width = track.width
                height = track.height
                codec = track.codec
                frame_rate = track.frame_rate

                video_info.append((width, height, codec, frame_rate))
                video_files.append(video_path)
                break  # Exit after processing the video track

# Check if all videos have the same properties
if all(info == video_info[0] for info in video_info):
    print("All videos have the same width, height, codec, and frame rate! JOINING VIDEOS...")

    # Sort the video files alphabetically
    video_files.sort()

    # Load the videos
    video_clips = [VideoFileClip(video).without_audio() for video in video_files]

    # Concatenate the videos
    final_video = concatenate_videoclips(video_clips)

    # Load the audio file
    audio_clip = AudioFileClip(audio_file)

    # Loop the audio if it's shorter than the final video duration
    if audio_clip.duration < final_video.duration:
        audio_clip = audio_clip.fx(vfx.loop, duration=final_video.duration)

    # Set the audio to the final video
    final_video = final_video.set_audio(audio_clip)

    # Write the result to a file
    output_file = os.path.join(video_directory, "output_video_with_audio.mp4")
    final_video.write_videofile(output_file, codec="libx264")

else:
    print("Not all videos have the same width, height, codec, and frame rate.")
