from PIL import Image
from brightness import get_average_brightness, get_pixel_brightness
from dir_to_img_list import load_images_in_directory, combine_images, order_images_by_brightness

covers = load_images_in_directory('album_covers')
brightnesses = [get_average_brightness(img) for img in covers]
pixel_brightnesses = get_pixel_brightness('test.png')
ordered_images = order_images_by_brightness(pixel_brightnesses, brightnesses, covers)

combine_images(ordered_images, '.', 'mario_covers.jpg')
