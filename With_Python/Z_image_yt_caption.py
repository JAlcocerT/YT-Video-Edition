from PIL import Image
import os
import io

# Define the target folder and max file size in bytes
folder_path = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"
max_size_bytes = 1.95 * 1024 * 1024  # 1.95MB to ensure it's under 2MB

# Find the .jpg file in the folder
jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
if not jpg_files:
    raise ValueError("No .jpg files found in the specified folder.")
elif len(jpg_files) > 1:
    raise ValueError("Multiple .jpg files found. Please ensure only one is present.")
image_path = os.path.join(folder_path, jpg_files[0])

# Open the image and check its current size
with Image.open(image_path) as img:
    # Get the current size in bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG', quality=95)  # Save at high quality to check initial size
    current_size = img_bytes.tell()

    # Resize the image if it's above the target size
    if current_size > max_size_bytes:
        # Set initial quality and resize factor
        quality = 95  # Start with high quality and reduce gradually
        resize_factor = 0.9  # Start with a slight reduction and iterate

        while current_size > max_size_bytes:
            # Apply resizing while maintaining aspect ratio
            new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
            img_resized = img.resize(new_size, Image.LANCZOS)

            # Check size in memory for resized image
            img_bytes = io.BytesIO()
            img_resized.save(img_bytes, format='JPEG', quality=quality)
            current_size = img_bytes.tell()

            # Gradually decrease quality and resize factor
            quality -= 5
            resize_factor -= 0.05

            # Avoid going below 10% quality or shrinking too small
            if quality < 10 or resize_factor < 0.2:
                break

        # Save the final resized image with the original name in the specified folder
        final_output_path = os.path.join(folder_path, "resized_image.jpg")
        img_resized.save(final_output_path, format='JPEG', quality=quality)
        print(f"Image resized and saved as resized_image.jpg with final size: {current_size / (1024 * 1024):.2f} MB")
    else:
        print("Image is already under 2MB; no resizing needed.")


# from PIL import Image
# import os

# # Define the target folder and max file size in bytes
# folder_path = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"
# max_size_bytes = 1.95 * 1024 * 1024  # 1.95MB to ensure it's under 2MB

# # Find the .jpg file in the folder
# jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
# if not jpg_files:
#     raise ValueError("No .jpg files found in the specified folder.")
# elif len(jpg_files) > 1:
#     raise ValueError("Multiple .jpg files found. Please ensure only one is present.")
# image_path = os.path.join(folder_path, jpg_files[0])

# # Temporary path for testing file size
# temp_path = os.path.join(folder_path, "temp.jpg")

# # Open the image and check its current size
# with Image.open(image_path) as img:
#     # Initial save to check file size
#     img.save(temp_path, format='JPEG')
#     current_size = os.path.getsize(temp_path)

#     # Resize the image if it's above the target size
#     if current_size > max_size_bytes:
#         # Set initial quality and resize factor
#         quality = 95  # Start with high quality and reduce gradually
#         resize_factor = 0.9  # Start with a slight reduction and iterate

#         while current_size > max_size_bytes:
#             # Apply resizing while maintaining aspect ratio
#             new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
#             img_resized = img.resize(new_size, Image.LANCZOS)

#             # Save the resized image to check if it meets the size requirement
#             img_resized.save(temp_path, format='JPEG', quality=quality)
#             current_size = os.path.getsize(temp_path)

#             # Gradually decrease quality and resize factor
#             quality -= 5
#             resize_factor -= 0.05

#             # Avoid going below 10% quality or shrinking too small
#             if quality < 10 or resize_factor < 0.2:
#                 break

#         # Save the final resized image with the original name in the specified folder
#         final_output_path = os.path.join(folder_path, "resized_image.jpg")
#         img_resized.save(final_output_path, format='JPEG', quality=quality)
#         print(f"Image resized and saved as resized_image.jpg with final size: {current_size / (1024 * 1024):.2f} MB")
#     else:
#         print("Image is already under 2MB; no resizing needed.")


# # from PIL import Image
# # import os

# # # Define the target folder and max file size in bytes
# # folder_path = "/media/jalcocert/BackUp/Z_BackUP_HD-SDD/OA5Pro/Z_Roma-29oct-2nov/ForoImperial/"
# # max_size_bytes = 1.95 * 1024 * 1024  # 2MB

# # # Find the .jpg file in the folder
# # jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
# # if not jpg_files:
# #     raise ValueError("No .jpg files found in the specified folder.")
# # elif len(jpg_files) > 1:
# #     raise ValueError("Multiple .jpg files found. Please ensure only one is present.")
# # image_path = os.path.join(folder_path, jpg_files[0])

# # # Open the image and check its current size
# # with Image.open(image_path) as img:
# #     # Initial save to check file size
# #     img.save("temp.jpg", format='JPEG')
# #     current_size = os.path.getsize("temp.jpg")

# #     # Resize the image if it's above the target size
# #     if current_size > max_size_bytes:
# #         # Set initial quality and resize factor
# #         quality = 95  # Start with high quality and reduce gradually
# #         resize_factor = 0.9  # Start with a slight reduction and iterate

# #         while current_size > max_size_bytes:
# #             # Apply resizing while maintaining aspect ratio
# #             new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
# #             img_resized = img.resize(new_size, Image.LANCZOS)

# #             # Save the resized image with reduced quality
# #             img_resized.save("temp.jpg", format='JPEG', quality=quality)
# #             current_size = os.path.getsize("temp.jpg")

# #             # Gradually decrease quality and resize factor
# #             quality -= 5
# #             resize_factor -= 0.05

# #             # Avoid going below 10% quality or shrinking too small
# #             if quality < 10 or resize_factor < 0.2:
# #                 break

# #         # Save the final resized image
# #         img_resized.save(os.path.join(folder_path, "resized_image.jpg"), format='JPEG', quality=quality)
# #         print(f"Image resized and saved as resized_image.jpg with final size: {current_size / (1024 * 1024):.2f} MB")
# #     else:
# #         print("Image is already under 2MB; no resizing needed.")
