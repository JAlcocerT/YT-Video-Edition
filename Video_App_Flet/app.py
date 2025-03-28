import flet as ft
import subprocess
import os

def main(page: ft.Page):
    page.title = "FFmpeg Task Runner"

    def run_ffmpeg(e):
        selected_option = option_dropdown.value
        directory = path_input.value

        if not os.path.isdir(directory):
            result_text.value = "Invalid directory path."
            page.update()
            return

        os.chdir(directory)  # Change the current working directory.

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
                result_text.value = "Join (Silenced) + Song completed."

            elif selected_option == "Extract images from video":

                video_file = next((f for f in os.listdir(directory) if f.lower().endswith(('.mp4', '.avi', '.mov'))), None) #finds the first video file in the directory.
                if video_file:
                    command = f'ffmpeg -i "{video_file}" -vf "select=\'gte(t\\,120)\',fps=1" -vsync vfr frame_%03d.png'
                else:
                    result_text.value = "No video file found in the specified directory."
                    page.update()
                    return

            else:
                result_text.value = "Invalid option selected."
                page.update()
                return

            subprocess.run(command, shell=True, check=True)
            result_text.value = f"{selected_option} completed successfully."

        except subprocess.CalledProcessError as e:
            result_text.value = f"Error: {e}"
        except FileNotFoundError:
            result_text.value = "FFmpeg not found. Ensure it's installed and in your PATH."
        except Exception as e:
            result_text.value = f"An unexpected error occurred: {e}"

        page.update()

    option_dropdown = ft.Dropdown(
        label="Select Option",
        options=[
            ft.dropdown.Option("Simply Join"),
            ft.dropdown.Option("Join (Silenced) + Song"),
            ft.dropdown.Option("Extract images from video"),
        ],
        value="Simply Join",
    )

    path_input = ft.TextField(label="Directory Path", value=os.getcwd())
    run_button = ft.ElevatedButton("Run", on_click=run_ffmpeg)
    result_text = ft.Text("")

    page.add(
        option_dropdown,
        path_input,
        run_button,
        result_text,
    )

ft.app(target=main)