import numpy as np
import cv2

#Black Image
img = np.zeros((512,512,3), np.uint8)

#Diagnol blue line
cv2.line(img, (0,0), (511,511), (255,0,0), 5)

#Green rectangle
cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

#Red Circle
cv2.circle(img, (447,63), 63, (0,0,255), -1)

#Ellipse
cv2.ellipse(img, (256,256), (100,50), 0, 0, 360, (255,0,0), -1)

#Drawing Polygon
pts = np.array([[20,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))

#Add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Rishabh', (10, 500), font, 4, (25,200,2), 2)

#Display Image
cv2.imshow('image', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
