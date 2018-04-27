import cv2
import numpy as np

while(1):
    img = cv2.imread('pinki.jpeg')

    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    
    pink_min = np.uint8([[[233, 5, 150]]])
    pink_max = np.uint8([[[339,73,100]]])
    mask = cv2.inRange(hsv_img, cv2.cvtColor(pink_min,cv2.COLOR_BGR2HSV), cv2.cvtColor(pink_max,cv2.COLOR_BGR2HSV))

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    # cv2.imwrite('output3.jpeg', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
