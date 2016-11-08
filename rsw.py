
import numpy as np
import cv2

#Load an color image in grayscale
image_path = '/home/rishabh/Downloads/FREC_Scab_3532_resized.JPG'
img = cv2.imread(image_path,0)

#Crete a named window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)#Window_normal allows resizing

# Display Image
cv2.imshow('image',img)
cv2.waitKey(1000)
cv2.imwrite('leafgray.png',img)
cv2.destroyAllWindows()


