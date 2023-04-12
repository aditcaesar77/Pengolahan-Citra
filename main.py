import cv2

from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("gambar/lena.jpg")

cv2.imshow('Gambar Asli', img)
waitKey(0)
