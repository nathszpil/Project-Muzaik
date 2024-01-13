from PIL import Image


def get_average_brightness(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Convert the grayscale image to a NumPy array
    grayscale_array = list(grayscale_image.getdata())

    # Calculate the average brightness
    average_brightness = sum(grayscale_array) / len(grayscale_array)

    return average_brightness


# Example usage
image_path = 'path/to/your/image.jpg'
avg_brightness = get_average_brightness(image_path)
print(f"Average Brightness: {avg_brightness}")
