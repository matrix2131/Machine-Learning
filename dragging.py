import cv2
import numpy as np
import matplotlib.pyplot as plt




#################
## VARIABLES ####
#################

# Initially drawing is taken as false and it will become true if a mouse button is clicked.

drawing = False
ix, iy = -1, -1


# FUNCTION
def draw_rectangle(event,x,y,flags,param):
    
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        drawing == True
        ix, iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (255,0,0), -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        cv2.rectangle(img, (ix,iy), (x,y), (255,0,0), -1)

# SHOWING THE IMAGE

# BLACK
img = np.zeros((512,512,3))

cv2.namedWindow(winname = "DRAWING")

cv2.setMouseCallback("DRAWING", draw_rectangle)

while True:
    cv2.imshow("DRAWING",img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()