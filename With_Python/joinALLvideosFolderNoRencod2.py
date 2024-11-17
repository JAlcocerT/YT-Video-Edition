import os
import subprocess

def join_videos_ffmpeg(video_directory, output_directory, output_filename="output_video.mp4"):
    """
    Joins all video files in a folder using FFmpeg without reencoding (fast method).

    Args:
        video_directory (str): Path to the folder containing video files.
        output_directory (str): Path to the folder where the output video will be saved.
        output_filename (str): Name of the output video file (default: "output_video.mp4").
    """
    # Create a file list for ffmpeg
    file_list_path = os.path.join(video_directory, "file_list.txt")
    
    with open(file_list_path, "w") as file:
        # Write the video files paths in the required ffmpeg format
        for filename in sorted(os.listdir(video_directory)):
            if filename.endswith(".MP4"):  # Make sure it's a video file
                file.write(f"file '{os.path.join(video_directory, filename)}'\n")

    # Prepare the output file path
    output_path = os.path.join(output_directory, output_filename)

    # Concatenate videos with FFmpeg (no reencoding)
    ffmpeg_command = [
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", file_list_path,
        "-c", "copy", output_path
    ]

    # Execute the FFmpeg command
    subprocess.run(ffmpeg_command, check=True)
    print(f"Videos successfully concatenated and saved as: {output_path}")

    # Clean up the temporary file list
    os.remove(file_list_path)

# # Example usage
# video_directory = r"C:\path\to\your\videos"  # Path to the folder containing videos
# output_directory = r"C:\path\to\output\folder"  # Path to the folder to save the output
# join_videos_ffmpeg(video_directory, output_directory)

# Example usage
video_directory = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"  # Path to the folder containing videos
output_directory = r"C:\Users\j--e-\Desktop\DJiOA5Pro-NL\NL-17nov"  # Path to the folder to save the output
join_videos_ffmpeg(video_directory, output_directory)