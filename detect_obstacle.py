

def preprocess_image(frame):
    import cv2
    import numpy as np
    frame = cv2.imread(frame)

    pink = np.uint8([[[147,20,255]]])
    hsv_pink = cv2.cvtColor(pink,cv2.COLOR_BGR2HSV)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([hsv_pink[0][0][0]-20,147,147])
    upper_bound = np.array([hsv_pink[0][0][0]+20,255,255])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    cv2.imwrite('res.jpeg', mask)

preprocess_image('pink.jpeg')