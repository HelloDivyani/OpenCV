import numpy as np
import cv2
from matplotlib import pyplot as plt

image_path = '/home/rishabh/Downloads/FREC_Scab_3532_resized.JPG'
img = cv2.imread(image_path, 0)
plt.imshow(img, cmap='gray', interpolation = 'bicubic')
plt.show()

