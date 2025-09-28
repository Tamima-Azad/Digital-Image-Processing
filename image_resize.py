import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def resize_image_manual(image, mew_width,new_height):
  original_width, original_height = image.size
  # Create a new image with swithched dimensions
  resized_image = Image.new("RGB", (new_width, new_height))
  # Rotate the image by rearanging pixels
  for y in range(new_height):
    for x in range(new_width):
      orig_x=int(x*original_width/new_width)
      orig_y=int(y* original_height/new_height)

      resized_image.putpixel((x,y),image.getpixel((orig_x,orig_y)))

  return resized_image
#Load the color image
input_image_path=r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"
image = Image.open(input_image_path)
new_width=200
new_height=200
resized_image=resize_image_manual(image, new_width, new_height)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(resized_image)
plt.title(f'Resized Image ({new_width}x{new_height})')
plt.axis('off')

plt.tight_layout()
plt.show()
