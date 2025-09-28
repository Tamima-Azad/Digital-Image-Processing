import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\ASUS\Desktop\image mid\images\face grayscale.jpg")
array = np.array([[255, 0, 1, 100, 25, 101],[10, 200, 70, 80, 120, 150,],[95, 30, 30, 81, 96, 77],[87, 89, 220, 250, 100, 10],[18, 7, 221, 21, 8, 15]])
img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_CL= img_gray.copy()
temp= img_gray.copy()
max_pixel = np.max(array)
L = 2**(np.ceil (np.log2(max_pixel)))
C=L/np.log(1+L)
height = img_gray.shape[0]
width = img_gray. shape[1]
for i in range(0, height):
  for j in range(0, width):
    img_gray[i][j]=np.log(1+img_gray[i][j])
    img_gray_CL[i][j]=C*img_gray[i][j]

plt.figure(figsize=(10,10))
plt.subplot(1,3,1)
plt.title('Original Image')
plt.imshow(temp, cmap='gray')
plt.subplot(1,3,2)
plt.imshow(img_gray, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(img_gray_CL, cmap='gray')
plt.title('Logarithmic C=L/log(1+L)')

img_gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height = img_gray.shape[0]
width = img_gray. shape[1]
r= np.unique(img_gray)
s1 = np.zeros(len(r))
s2 = np.zeros(len(r))
for i in range(0, len(r)):
  s1[i]=np.log(1+r[i])
  s2[i]=C*s1[i]
plt.figure(figsize=(5,5))
plt.subplot(1,2,1)
plt.plot(r,s1)
plt.title('Logarithmic C=1')
plt.subplot(1,2,2)
plt.plot(r,s2)
plt.title('Logarithmic C=L/log(1+L)')
plt.xlabel('r')
plt.ylabel('s')
plt.xlim([0, max_pixel])
plt.ylim([0, max_pixel])
plt.grid()
plt.show()