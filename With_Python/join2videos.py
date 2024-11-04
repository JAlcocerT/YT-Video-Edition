#python3 join2videos.py

from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define the directory where the videos are located
video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"

# Load the videos
video1 = VideoFileClip(video_directory + "DJI_20241030132520_0026_D.MP4")
video2 = VideoFileClip(video_directory + "DJI_20241030145603_0036_D.MP4")

# Concatenate the videos
final_video = concatenate_videoclips([video1, video2])

# Write the result to a file
final_video.write_videofile("output_video.mp4", codec="libx264")


# from moviepy.editor import VideoFileClip, concatenate_videoclips

# # Load the videos
# video1 = VideoFileClip("video1.mp4")
# video2 = VideoFileClip("video2.mp4")

# # Concatenate the videos
# final_video = concatenate_videoclips([video1, video2])

# # Write the result to a file
# final_video.write_videofile("output_video.mp4", codec="libx264")
