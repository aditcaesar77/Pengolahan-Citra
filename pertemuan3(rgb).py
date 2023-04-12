import cv2

from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("gambar/lena.jpg")
H, W = img.shape[:2]
gray = np.zeros((H, W), np.uint8)
for i in range(H):
    for j in range(W):
        gray[i,j]= np.clip(0.299 * img[i, j, 2] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 0], 0, 255)
fig = plt.figure()
fig.add_subplot(211)
plt.imshow(img)
fig.add_subplot(212)
plt.imshow(gray)
plt.show()