import numpy as np
import cv2
import matplotlib.pyplot as plt
arr = np.array([
    [255, 0, 1, 100, 25, 101],
    [10, 200, 70, 80, 120, 150],
    [95, 30, 30, 81, 96, 77],
    [87, 89, 220, 250, 100, 10],
    [18, 7, 221, 21, 8, 15],
    [10, 40, 33, 227, 189, 3]
], np.uint8)
temp = arr.copy()
arr = np.pad(arr, 1, 'constant', constant_values=0)
filter = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]) / 16
ans = arr.copy()
for i in range(1, arr.shape[0] - 1):
    for j in range(1, arr.shape[1] - 1):
        ans[i, j] = round(np.sum(arr[i - 1:i + 2, j - 1:j + 2] * filter))
ans = ans[1:ans.shape[0] - 1, 1:ans.shape[1] - 1]

print("Manual Convolution Result:\n", ans)
print()
conv2 = cv2.filter2D(arr, -1, filter)
conv2 = conv2[1:conv2.shape[0] - 1, 1:conv2.shape[1] - 1]
print("Built-in Convolution Result:\n", conv2)
plt.figure(figsize=(10, 10))
plt.subplot(1, 3, 1)
plt.imshow(temp, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(ans, cmap='gray')
plt.title('After Manual Convolution')
plt.subplot(1, 3, 3)
plt.imshow(conv2, cmap='gray')
plt.title('After Built-in Convolution')
plt.show()