from PIL import Image
import math

# Example usage:
image_path = "test.png"
image = Image.open(image_path)
colors = image.getcolors()

print("Colors and their counts:")
print(colors)


def euclidean_distance(color1, color2):
    # Extract RGB components
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    print(color1, color2)
    # Calculate Euclidean distance
    distance = math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

    return distance


color1 = colors[0][1][:-1]
color2 = colors[1][1][:-1]

distance = euclidean_distance(color1, color2)
print(f"The Euclidean distance between the two colors is: {distance}")
