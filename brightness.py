from PIL import Image
import numpy as np


def get_average_brightness(image):
    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Convert the grayscale image to a NumPy array
    grayscale_array = np.array(grayscale_image)

    # Calculate the average brightness
    average_brightness = np.mean(grayscale_array)

    return average_brightness


def get_pixel_brightness(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Convert the grayscale image to a NumPy array
    grayscale_array = list(grayscale_image.getdata())

    # Calculate the brightness for each pixel
    brightness_values = [pixel for pixel in grayscale_array]

    return brightness_values
