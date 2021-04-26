import cv2
import numpy as np
import matplotlib.pyplot as plt


def draw_circle(event,x,y,flags,param):  # The parameters are automatically taken by openCV.
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 100, (255,0,0), -1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y), 100, (0,255,0), -1)


cv2.namedWindow(winname ="MY_DRAWING")

cv2.setMouseCallback("MY_DRAWING",draw_circle)

# This is the way of joining the function with image being taken in.



#######################################
##### SHOWING IMAGE WITH OPENCV   #####
#######################################


img = np.zeros((512,512,3))

while True:
    cv2.imshow("MY_DRAWING", img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()