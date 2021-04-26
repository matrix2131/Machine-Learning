import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWM:
        cv2.circle(img,(x,y), 50, (255,0,0) , 8)
    
cv2.namedWindow(winname = "CIRCLES")
cv2.setMouseCallback("CIRCLES", draw_circle)

img = cv2.imread("/home/soniya/Documents/work/Computer-Vision-with-Python/DATA/dog_backpack.jpg")

while True:
    cv2.imshow("CIRCLES", img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()