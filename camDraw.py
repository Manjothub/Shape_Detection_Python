import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('shape10.png')
# img = cv2.imread('moni.jpeg')

height, width, channels = img.shape
print (height, width, channels)