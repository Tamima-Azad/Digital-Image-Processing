import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
input_image_path =r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"
image = Image.open(input_image_path)
image_np = np.array(image)

# Separate the color components
red_component = image_np.copy()
green_component = image_np.copy()
blue_component = image_np.copy()

# Set other channels to zero
red_component[:, :, 1] = 0 # Zero out green channel
red_component[:, :, 2] = 0 # Zero out blue channel
green_component[:, :, 0] = 0 # Zero out red channel
green_component[:, :, 2] = 0 # Zero out blue channel
blue_component[:, :, 0] = 0 # Zero out red channel
blue_component[:, :, 1] = 0 # Zero out green channel

# Create images for each color component
red_image = Image.fromarray(red_component)
green_image = Image.fromarray(green_component)
blue_image = Image.fromarray(blue_component)

# Reconstruct the original image
reconstructed_image = Image.fromarray(image_np)

# Display the original and the separated color components
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.imshow(red_image)
plt.title('Red Component')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(green_image)
plt.title('Green Component')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(blue_image)
plt.title('Blue Component')
plt.axis('off')

plt.subplot(2, 2, 4)
# Missing code from original image to display the reconstructed image, assuming it would be similar to:
plt.imshow(reconstructed_image)
plt.title('Reconstructed Image')
plt.axis('off')

plt.tight_layout()
plt.show()