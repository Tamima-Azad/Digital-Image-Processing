import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
input_image_path =r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"
image = Image.open(input_image_path)
image_np = np.array(image)

# Define the color range for green (in RGB format)
lower_green = np.array([100, 0, 0]) # Lower bound (R, G, B)
upper_green = np.array([255, 100, 100]) # Upper bound (R, G, B)

# Create a mask for green pixels
mask = np.all((image_np >= lower_green) & (image_np <= upper_green), axis=-1)

# Create an output image where only the green pixels are retained
output_image_np = np.zeros_like(image_np)
output_image_np[mask] = image_np[mask]

# Convert the output image back to PIL format
output_image = Image.fromarray(output_image_np)

# Plot the original and filtered images side by side
plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(output_image)
plt.title('Filtered Image (Green Pixels)')
plt.axis('off')

plt.tight_layout()
plt.show()