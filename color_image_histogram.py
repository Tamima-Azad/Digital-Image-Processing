import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Load the color image
input_image_path = r"C:\Users\ASUS\Desktop\image mid\images\RGB_image.jpg"
image = Image.open(input_image_path)
image_np = np.array(image)

# Calculate the histogram for each color channel
red_channel = image_np[:, :, 0]
green_channel = image_np[:, :, 1]
blue_channel = image_np[:, :, 2]

# Calculate histograms
red_hist, bins_red = np.histogram(red_channel.flatten(), bins=256, range=[0, 256])
green_hist, bins_green = np.histogram(green_channel.flatten(), bins=256, range=[0, 256])
blue_hist, bins_blue = np.histogram(blue_channel.flatten(), bins=256, range=[0, 256])


plt.figure(figsize=(12,6))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Histogram
plt.subplot(1, 2, 2)

plt.plot(bins_red[:-1], red_hist, color='red', label='Red Channel')
plt.plot(bins_green[:-1], green_hist, color='green', label='Green Channel')
plt.plot(bins_blue[:-1], blue_hist, color='blue', label='Blue Channel')

plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.xlim([0, 255])
plt.tight_layout()
plt.show()