# # ### python3 join2videos_flip_silencewatermark.py


#Add the watermark with ffmpeg for now (choosing number of cores as well!)
#JAlcocerTech_xyz_logo-watermark.png
#ffmpeg -i output_video_2688x1512_59.940fps.mp4 -i JAlcocerTech_xyz_logo-watermark.png -filter_complex "overlay=W-w-10:H-h-10" -c:v libx264 -crf 18 -preset veryfast -c:a copy output_video_with_watermark.mp4
#ffmpeg -i output_video_2688x1512_59.940fps.mp4 -i JAlcocerTech_xyz_logo-watermark.png -filter_complex "overlay=W-w-10:H-h-10" -c:v libx264 -crf 18 -preset veryfast -c:a copy -threads 5 output_video_with_watermark.mp4


import os
from pymediainfo import MediaInfo
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioClip

# Define the directory where the videos are located
video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/Trastevere/"

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

    # Load the videos without audio
    video_clips = [VideoFileClip(video).without_audio() for video in video_files]

    # Concatenate the videos
    final_video = concatenate_videoclips(video_clips)

    # Create a silent audio clip with the same duration as the final video
    silent_audio = AudioClip(lambda t: 0, duration=final_video.duration)

    # Set the silent audio to the final video
    final_video = final_video.set_audio(silent_audio)

    # Get the width, height, and frame rate for the output filename
    width, height, _, frame_rate = video_info[0]
    # Using frame_rate as a float and formatting it for the filename
    frame_rate_float = float(frame_rate)
    output_file_name = f"output_video_{width}x{height}_{frame_rate_float:.3f}fps.mp4"
    output_file = os.path.join(video_directory, output_file_name)

    print("Saving the video as =>>> ", output_file)
    final_video.write_videofile(output_file, codec="libx264")
else:
    print("Not all videos have the same width, height, codec, and frame rate.")