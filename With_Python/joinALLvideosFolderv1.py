import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def join_videos_in_folder(video_directory, output_folder=".", output_filename="output_video.mp4"):
    """
    Joins all video files found in a specific folder into one final video.

    Args:
        video_directory (str): Path to the folder containing video files.
        output_folder (str): Path to the folder where the final video will be saved (default: current folder).
        output_filename (str): Name of the output video file (default: "output_video.mp4").
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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
        final_video = concatenate_videoclips(video_clips)
        # Create the full path for the output video
        output_path = os.path.join(output_folder, output_filename)
        # Write the result to a file
        final_video.write_videofile(output_path, codec="libx264")
        print(f"Final video saved as: {output_path}")
    else:
        print("No video files found in the specified directory.")

### Example usage for Windows
video_directory_win = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL"  # Windows path example
output_folder_win = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL"  # Specify the output folder
join_videos_in_folder(video_directory_win, output_folder=output_folder_win)

### Example usage for Linux
# video_directory_linux = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"  # Linux path example
# output_folder_linux = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/FinalVideos"  # Specify the output folder
# join_videos_in_folder(video_directory_linux, output_folder=output_folder_linux)


# #python joinALLvideosFolder.py

# import os
# from moviepy.editor import VideoFileClip, concatenate_videoclips

# def join_videos_in_folder(video_directory, output_filename="output_video.mp4"):
#     """
#     Joins all video files found in a specific folder into one final video.

#     Args:
#         video_directory (str): Path to the folder containing video files.
#         output_filename (str): Name of the output video file (default: "output_video.mp4").
#     """
#     # List to store the video clips
#     video_clips = []

#     # Loop through the files in the directory
#     for filename in os.listdir(video_directory):
#         if filename.endswith(".MP4"):  # Check if the file is a video (you can add other extensions)
#             video_path = os.path.join(video_directory, filename)
#             print(f"Loading video: {video_path}")
#             video_clips.append(VideoFileClip(video_path))

#     # Concatenate the videos
#     if video_clips:
#         final_video = concatenate_videoclips(video_clips)
#         # Write the result to a file
#         final_video.write_videofile(output_filename, codec="libx264")
#         print(f"Final video saved as: {output_filename}")
#     else:
#         print("No video files found in the specified directory.")

# ### Example usage for Windows
# video_directory_win = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL"  # Windows path example
# join_videos_in_folder(video_directory_win)

# ### Example usage for Linux
# # video_directory_linux = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"  # Linux path example
# # join_videos_in_folder(video_directory_linux)