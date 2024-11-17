#python joinALLvideosFolderNoRencod.py

import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def join_videos_in_folder(video_directory, output_directory, output_filename="output_video.mp4"):
    """
    Joins all video files found in a specific folder into one final video without reencoding.

    Args:
        video_directory (str): Path to the folder containing video files.
        output_directory (str): Path to the folder where the output video will be saved.
        output_filename (str): Name of the output video file (default: "output_video.mp4").
    """
    # List to store the video clips
    video_clips = []

    # Loop through the files in the directory
    for filename in os.listdir(video_directory):
        if filename.endswith(".MP4"):  # Check if the file is a video (you can add other extensions)
            video_path = os.path.join(video_directory, filename)
            print(f"Loading video: {video_path}")
            video_clips.append(VideoFileClip(video_path))

    # Concatenate the videos
    if video_clips:
        final_video = concatenate_videoclips(video_clips, method="compose")  # method='compose' prevents reencoding
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Create the full path for the output file
        output_path = os.path.join(output_directory, output_filename)
        
        # Write the result to a file
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=4)
        print(f"Final video saved as: {output_path}")
    else:
        print("No video files found in the specified directory.")

# Example usage
video_directory = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"  # Path to the folder containing videos
output_directory = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"  # Path to the folder to save the output
join_videos_in_folder(video_directory, output_directory)