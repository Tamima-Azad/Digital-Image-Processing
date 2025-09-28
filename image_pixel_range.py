import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the color image
input_image_path = r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"  # Replace with your image path
image = Image.open(input_image_path)
image_np = np.array(image)

# keep only red pixels (you can adjust this)
lower_color = np.array([0, 0, 0])  # Lower bound (R, G, B)
upper_color = np.array([100, 255, 100])  # Upper bound (R, G, B)

# Create a mask for pixels within the specified color range
mask = np.all((image_np >= lower_color) & (image_np <= upper_color), axis=-1)

# Create an output image where only the specified color pixels are retained
output_image_np = np.zeros_like(image_np)
output_image_np[mask] = image_np[mask]

# Convert the output image back to PIL format
output_image = Image.fromarray(output_image_np)

#Plot the original and filtered images side by side
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(output_image)
plt.title('Filtered Image (Color Range)')
plt.axis('off')

plt.tight_layout()
plt.show()