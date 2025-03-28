import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os

def run_ffmpeg():
    selected_option = option_dropdown.get()
    directory = path_entry.get()

    if not os.path.isdir(directory):
        messagebox.showerror("Error", "Invalid directory path.")
        return

    os.chdir(directory)

    try:
        if selected_option == "Simply Join":
            command = f'ffmpeg -i "concat:$(ls *.mp4 | tr \'\\n\' \'|\')" -c copy output_video.mp4'
        elif selected_option == "Join (Silenced) + Song":
            command1 = 'ls *.MP4 | sed "s/^/file \'/; s/$/\'/" > file_list.txt'
            command2 = 'ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an silenced_output_video.mp4'
            command3 = 'ffmpeg -stream_loop -1 -i "AETHER - Density & Time.mp3" -i silenced_output_video.mp4 -c:v copy -c:a aac -shortest output_with_song.mp4'
            subprocess.run(command1, shell=True, check=True)
            subprocess.run(command2, shell=True, check=True)
            subprocess.run(command3, shell=True, check=True)
            result_label.config(text="Join (Silenced) + Song completed.")

        elif selected_option == "Extract images from video":
            video_file = next((f for f in os.listdir(directory) if f.lower().endswith(('.mp4', '.avi', '.mov'))), None)
            if video_file:
                command = f'ffmpeg -i "{video_file}" -vf "select=\'gte(t\\,120)\',fps=1" -vsync vfr frame_%03d.png'
            else:
                messagebox.showerror("Error", "No video file found in the specified directory.")
                return
        else:
            messagebox.showerror("Error", "Invalid option selected.")
            return

        subprocess.run(command, shell=True, check=True)
        result_label.config(text=f"{selected_option} completed successfully.")

    except subprocess.CalledProcessError as e:
        result_label.config(text=f"Error: {e}")
    except FileNotFoundError:
        result_label.config(text="FFmpeg not found. Ensure it's installed and in your PATH.")
    except Exception as e:
        result_label.config(text=f"An unexpected error occurred: {e}")

def browse_directory():
    directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, directory)

root = tk.Tk()
root.title("FFmpeg Task Runner")

option_label = tk.Label(root, text="Select Option:")
option_label.pack()

options = ["Simply Join", "Join (Silenced) + Song", "Extract images from video"]
option_dropdown = ttk.Combobox(root, values=options, state="readonly")
option_dropdown.current(0)
option_dropdown.pack()

path_label = tk.Label(root, text="Directory Path:")
path_label.pack()

path_frame = tk.Frame(root)
path_frame.pack()

path_entry = tk.Entry(path_frame, width=50)
path_entry.insert(0, os.getcwd())
path_entry.pack(side=tk.LEFT)

browse_button = tk.Button(path_frame, text="Browse", command=browse_directory)
browse_button.pack(side=tk.LEFT)

run_button = tk.Button(root, text="Run", command=run_ffmpeg)
run_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()