### python3 join2videos_flip.py

#ffmpeg -i output_video4.mp4 -an -c:v copy silenced_video.mp4
#ffmpeg -i silenced_video.mp4 -stream_loop -1 -i "Temple Of Freedom - Hanu Dixit.mp3" -c:v copy -c:a aac -shortest final_output_video.mp4


import os
import subprocess
from pymediainfo import MediaInfo
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define the directory where the videos are located
#video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"
video_directory = "/home/jalcocert/Desktop/oa5/MRK/Video1/Intro"

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
    video_clips = [VideoFileClip(video) for video in video_files]

    # Concatenate the videos
    final_video = concatenate_videoclips(video_clips)

    # Write the result to a file
    final_video.write_videofile("output_video4.mp4", codec="libx264")
else:
    print("Not all videos have the same width, height, codec, and frame rate.")



# from moviepy.editor import VideoFileClip, concatenate_videoclips

# # Define the directory where the videos are located
# video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"

# # Load the videos
# video1 = VideoFileClip(video_directory + "DJI_20241030144545_0034_D.MP4")
# video2 = VideoFileClip(video_directory + "DJI_20241030145603_0036_D.MP4")

# # Flip the second video 180 degrees - No need to flip here!!!
# #video2_flipped = video2.rotate(180)

# # Concatenate the videos
# final_video = concatenate_videoclips([video1, video2])

# # Write the result to a file
# final_video.write_videofile("output_video3.mp4", codec="libx264")