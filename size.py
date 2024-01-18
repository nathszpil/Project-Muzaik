from PIL import Image
import os
from dir_to_img_list import load_images_in_directory


def resize_images(images, output_directory, target_width, target_height):
    for i, image in enumerate(images):
        # Resize the image
        resized_image = image.resize((target_width, target_height), Image.BICUBIC)

        # Get the original filename without extension
        filename_without_extension = str(i)

        # Create a new filename for the resized image
        output_filename = f"{filename_without_extension}_resized.jpg"

        # Save the resized image with a unique filename
        output_path = os.path.join(output_directory, output_filename)
        resized_image.save(output_path)


# Example usage:
input_directory = "album_covers"
output_directory = "resized_images"
target_width = 500
target_height = 500

images = load_images_in_directory(input_directory)
# Resize the images
resize_images(images, output_directory, target_width, target_height)
