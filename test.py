import numpy as np
import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(0)  
while True:

    camWidth = 1920
    camheight = 1000


    ret, image = cap.read()
    image = cv2.resize(image, (camWidth, camheight))

    RED = (0, 0, 255)
    YELLOW = (0, 255, 255)
    thickness = 2
    radius = 25
    center = (200, 75)
    axes = (radius, radius)
    angle = 0
    startAngle = 180
    endAngle = 360

    # Draw a diagonal green line with thickness of 9 px
    cv2.line(image, (175, 75), (175, 275), RED, thickness)
    # Draw a diagonal green line with thickness of 9 px
    cv2.line(image, (225, 75), (225, 275), RED, thickness)

    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, RED, thickness)

    center = (200, 275)
    angle = 180
    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, RED, thickness)


    cv2.circle(image, (200, 100), 19, YELLOW, 1)
    cv2.circle(image, (200, 150), 19, YELLOW, 1)
    cv2.circle(image, (200, 200), 19, YELLOW, 1)
    cv2.circle(image, (200, 250), 19, YELLOW, 1)




    cv2.imshow("My Video", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()