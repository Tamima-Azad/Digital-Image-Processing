import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Generate random 24x24 grayscale image
# array = np.random.randint(0, 256, (24, 24), dtype=np.uint8)
# temp = array.copy()

input_image_path = r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"
image = Image.open(input_image_path)
array = np.array(image)
temp = array.copy()

# Manually calculate histogram using loop
hist = [0] * 256  # create a list of 256 bins initialized with 0
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        pixel_value = array[i, j]
        hist[pixel_value] += 1

# Plot image and histogram
plt.figure(figsize=(12, 5))

# Show image
plt.subplot(1, 2, 1)
plt.title("Original 24x24 Image")
plt.imshow(temp, cmap='gray')
plt.axis("off")

# Show histogram
plt.subplot(1, 2, 2)
plt.title("Histogram of Original (using loop)")
plt.bar(range(256), hist, color='blue', alpha=0.7, width=1.0)
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
