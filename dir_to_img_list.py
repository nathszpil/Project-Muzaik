from PIL import Image
import os


def load_images_in_directory(directory_path):
    # Get a list of all files in the directory
    all_files = os.listdir(directory_path)

    # Filter for image files (you can customize the list of valid extensions)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [file for file in all_files if any(file.lower().endswith(ext) for ext in image_extensions)]

    # Load each image using Pillow and return a list of Image objects
    images = [Image.open(os.path.join(directory_path, file)) for file in image_files]

    return images


def combine_images(image_list, output_directory, output_filename):
    # Calculate the dimensions of the square
    num_images = len(image_list)
    square_size = int(num_images ** 0.5)
    if square_size * square_size < num_images:
        square_size += 1

    # Get the dimensions of the first image in the list
    width, height = image_list[0].size

    # Create a new square image
    combined_image = Image.new('RGB', (width * square_size, height * square_size))

    # Paste each image onto the new image
    for i, image in enumerate(image_list):
        row = i // square_size
        col = i % square_size
        combined_image.paste(image, (col * width, row * height))

    # Save the combined image in the specified directory
    output_path = os.path.join(output_directory, output_filename)
    combined_image.save(output_path)


def order_images_by_brightness(pixel_brightnesses, brightnesses, covers):
    ordered_images = []

    for pixel_brightness in pixel_brightnesses:
        record = float('inf')
        img_index = 0

        for i in range(len(brightnesses)):
            difference = abs(brightnesses[i] - pixel_brightness)

            if difference < record:
                record = difference
                img_index = i

        ordered_images.append(covers[img_index])

    return ordered_images
