import imageio
import os

#pip install imageio
#sudo apt install python3-imageio


def create_gif(image_folder, output_gif_name, duration=0.1):
    """Creates a GIF from images in a folder.

    Args:
        image_folder: Path to the folder containing the images.
        output_gif_name: Name of the output GIF file.
        duration: Delay between frames in seconds (default: 0.1 seconds).
    """

    images = []
    for filename in sorted(os.listdir(image_folder)):  # Sort for consistent order
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Add other extensions if needed
            filepath = os.path.join(image_folder, filename)
            try:
                image = imageio.v2.imread(filepath)  # Use v2 for latest imageio
                images.append(image)
            except Exception as e:
                print(f"Error reading image {filename}: {e}")

    if images:
        imageio.v2.mimsave(output_gif_name, images, duration=duration, loop=0)  # loop=0 for infinite loop
        print(f"GIF created successfully: {output_gif_name}")
    else:
        print("No images found in the specified folder.")

# # Example usage:
# image_folder = "/home/jalcocert/Desktop/16jan-skijet-day/crash"  # Replace with your folder path
# output_gif_name = "output.gif"
# duration = 0.1  # 100 milliseconds between frames
# create_gif(image_folder, output_gif_name, duration)


# Example usage with error handling for the directory
image_folder = "/home/jalcocert/Desktop/16jan-skijet-day/crash"  # Replace with your folder path
output_gif_name = "output.gif"
duration = 0.1  # 100 milliseconds between frames

try:
    if os.path.exists(image_folder) and os.path.isdir(image_folder):
        create_gif(image_folder, output_gif_name, duration)
    else:
        raise FileNotFoundError(f"The specified directory '{image_folder}' does not exist or is not a directory.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")