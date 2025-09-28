import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def rotate_image_90(image, direction="clockwise"):
    width, height = image.size
    new_image = Image.new("RGB", (height, width))

    for y in range(height):
        for x in range(width):
            if direction == "clockwise":
                # (x,y) -> (height-1-y, x)
                new_image.putpixel((height - 1 - y, x), image.getpixel((x, y)))
            elif direction == "anticlockwise":
                # (x,y) -> (y, width-1-x)
                new_image.putpixel((y, width - 1 - x), image.getpixel((x, y)))
            else:
                raise ValueError("Direction must be 'clockwise' or 'anticlockwise'")

    return new_image
input_image_path=r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"
image = Image.open(input_image_path)
rotated_cw = rotate_image_90(image, "clockwise")
rotated_ccw = rotate_image_90(image, "anticlockwise")

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(image)
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(rotated_cw)
plt.title('90° Clockwise')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(rotated_ccw)
plt.title('90° Anticlockwise')
plt.axis('off')

plt.tight_layout()
plt.show()