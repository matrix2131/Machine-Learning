import cv2
import matplotlib.pyplot as plt
import numpy as np
def display(img,cmap = 'gray'):
    fig = plt.figure(figsize = (12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
road = cv2.imread("/home/soniya/Documents/work/Computer-Vision-with-Python/DATA/road_image.jpg")
road_copy = np.copy(road)
marker_image = np.zeros(road.shape[:2], dtype = np.int32)
segments = np.zeros(road.shape, dtype = np.uint8)
from matplotlib import cm
def create_rgb(i):
    return tuple(np.array(cm.tab10(0)[:3])*255)
colors = []
for i in range(10):
    colors.append(create_rgb(i))

n_markers = 10  
current_marker = 1


marks_updated = False


def mouse_callback(event,x,y,flags,param):
    global marks_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
       
        cv2.circle(marker_image, (x,y), 10,(current_marker),-1)
    
    
        cv2.cirlce(road_copy,(x,y),10,colors[current_marker],-1)
        
        marks_updated = True

cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    
    cv2.imshow('Watershed Segments',segments)
    cv2.imshow('Road Image', road_copy)
    
   
    k = cv2.waitKey(1)
    if k ==27:
        break
        
   
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype = np.int32)
        segments = np.zeros(road.shape, dtype = np.uint8)
        
        
   
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
        
        
    
    if marks_updated:
        
        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)
        
        segments = np.zeros(road.shape, dtype = np.uint8)
        
        for color_ind in range(n_markers):
         
            segments[marker_image_copy == (color_ind)] = colors[color_ind] 
        
cv2.destrotAllWindows()   
    