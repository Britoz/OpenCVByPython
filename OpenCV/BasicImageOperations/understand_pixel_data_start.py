# Demonstrate the understanding pixel data
import numpy as np
import cv2

# TODO: open an image
img = cv2.imread("../Images/girl1.PNG", 1)
print("Type of the image: ", type(img))
print("Length of image: ", len(img))

print("Length of first line image: ", len(img[0]))
print("Length of first value of image: ", len(img[0][0]))
print("Shape of image: ", img.shape)
print(img.dtype)

'''
descript: the image is built by an byte value
'''
print(img[:, :, 0])
print("Size of image: ", img.size)