# #python3 join2videos_flip.py


from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define the directory where the videos are located
video_directory = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"

# Load the videos
video1 = VideoFileClip(video_directory + "DJI_20241030144545_0034_D.MP4")
video2 = VideoFileClip(video_directory + "DJI_20241030145541_0035_D.MP4")

# Flip the second video 180 degrees
video2_flipped = video2.rotate(180)

# Concatenate the videos
final_video = concatenate_videoclips([video1, video2_flipped])

# Write the result to a file
final_video.write_videofile("output_video2.mp4", codec="libx264")