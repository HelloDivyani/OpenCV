import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True
ix, iy = -1, -1

def nothing(x):
    pass

# mouse callback
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x,y), rad, (b,g,r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x,y), rad, (b,g,r),-1)


# Create a white image
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
# Create trackbar for radius and color change
cv2.createTrackbar('Radius', 'image', 0, 100, nothing)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    global rad, r, g, b
    rad = cv2.getTrackbarPos('Radius', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    

cv2.destroyAllWindows()
