# import numpy as np
# import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(0)  
while True:

    # cam Size
    camWidth = 500
    camheight = 500

    camCenterW = camWidth / 2
    camCenterH = camheight / 2

    # var define
    RED = (0, 0, 255)
    YELLOW = (0, 255, 255)
    thickness = 2
    ellipseRadius = 25
    axes = (ellipseRadius, ellipseRadius)
    angle = 0
    startAngle = 180
    endAngle = 360

    ret, image = cap.read()
    image = cv2.resize(image, (camWidth, camheight))

    lineX1 = int(camCenterW - ellipseRadius)
    lineX2 = int(camCenterW + ellipseRadius)
    lineY1 = int(camCenterH - (ellipseRadius * 4))
    lineY2 = int(camCenterH + (ellipseRadius * 3))

    # print("start")
    # print(lineX1)
    # print(lineX2)
    # print(lineY1)
    # print(lineY2)

    cv2.line(image, (lineX1, lineY1), (lineX1, lineY2), RED, thickness)
    cv2.line(image, (lineX2, lineY1), (lineX2, lineY2), RED, thickness)


    center = (int(lineX1 + ellipseRadius), lineY1)

    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, RED, thickness)

    center = (int(lineX1 + ellipseRadius), lineY2)
    angle = 180
    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, RED, thickness)


    circleRadius = 19
    circleX = int(camCenterW)
    circleY = int(camCenterH)
    circleGap = 5

    # print(circleX)
    # print(circleY)

    cv2.circle(image, (circleX, int(circleY - circleRadius*4)), circleRadius, YELLOW, 1)
    cv2.circle(image, (circleX, int(circleY - circleRadius*2) + circleGap), circleRadius, YELLOW, 1)
    cv2.circle(image, (circleX, int(circleY) + circleGap*2), circleRadius, YELLOW, 1)
    cv2.circle(image, (circleX, int(circleY + circleRadius*2)+circleGap*3), circleRadius, YELLOW, 1)


    cv2.imshow("My Video", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()