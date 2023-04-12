import cv2

from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("gambar/lena.jpg")
waitKey(0)

#mengubah ke greyscale
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
brightness = 50
h, w = img2.shape[:2]

#perulangan untuk melakukan proses penambahan
for i in np.arange(h):
    for j in np.arange(w):
        a = img2.item(i, j)
        b = a + brightness
        
        if b > 255:
            b = 255
        elif b < 0:
            b = 0
        else:
            b = b
        img2.itemset((i, j), b)
cv2.imshow('Gambar Asli', img2)
waitKey(0)
