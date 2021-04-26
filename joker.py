import cv2

img = cv2.imread("/home/soniya/Desktop/Wallpapers/joker2.jpg")
while True:
    cv2.imshow("Image", img)
    # If we waited at least millisecond AND we have pressed the escape.
    if cv2.waitKey(1)  &  0xFF == 27:
        break
cv2.destroyAllWindows()