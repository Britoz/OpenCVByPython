# Demonstrate beginning of opencv in python

# TODO: import opencv and numpy
import numpy as np
import cv2

img = cv2.imread("../Images/girl1.PNG")
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow(
    "Image",
    img
)
'''

'''

cv2.waitKey(0)
cv2.imwrite("output.jpg", img)