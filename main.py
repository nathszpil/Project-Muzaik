from PIL import Image
from brightness import get_average_brightness, get_pixel_brightness
from dir_to_img_list import load_images_in_directory

covers = load_images_in_directory('album_covers')
brightnesses = [get_average_brightness(img) for img in covers]
pixel_brightnesses = get_pixel_brightness('test.png')
ordered_images = []

for pixel_brightness in pixel_brightnesses:
    record = 257
    i = 0
    for i in range(len(brightnesses)):
        if abs(brightnesses[i] - pixel_brightness) < record:
            record = brightnesses[i] - pixel_brightness
            img_index = i
    ordered_images.append(covers[i])

