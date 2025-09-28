import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\ASUS\Desktop\image mid\images\face grayscale.jpg")
img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp= img_gray.copy()
max_pixel = np.max(img_gray)
max_pixel = (2**(np.ceil(np.log2(max_pixel))))-1
height = img_gray.shape[0]
width = img_gray. shape[1]
for i in range(0, height):
  for j in range(0, width):
    img_gray[i][j]=max_pixel-img_gray[i][j]
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(temp, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(img_gray, cmap='gray')
plt.title('Negative Image')
r = np.unique(img_gray)
s = np.zeros(len(r))
for i in range(0, len(r)):
  s[i] = max_pixel-r[i]
plt.figure(figsize=(5,5))
plt.plot(r,s)
plt.title('Negative Image Transformation Curve')

plt.show()
