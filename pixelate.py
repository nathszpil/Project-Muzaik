from PIL import Image
import os


def pixelate(image_path, pixel_size):
    # Open the image
    image = Image.open(image_path)

    # Get the image size
    width, height = image.size

    # Resize the image to a smaller size
    small_image = image.resize((width // pixel_size, height // pixel_size), resample=Image.NEAREST)

    # Resize the small image back to the original size
    pixelated_image = small_image.resize((width, height), resample=Image.NEAREST)

    return pixelated_image


# Example usage
input_image_path = "mario_pixels.jpg"
pixel_size = 49

result = pixelate(input_image_path, pixel_size)

# Get the current working directory
current_directory = os.getcwd()

# Save the pixelated image in the current directory
output_image_path = os.path.join(current_directory, "pixelated_image.jpg")
result.save(output_image_path)
