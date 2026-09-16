import cv2
import numpy as np

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, width=640):
    h, w = image.shape[:2]
    if w <= width:
        return image
    ratio = width / w
    return cv2.resize(image, (width, int(h * ratio)))

def blur_image(gray, method="gaussian"):
    if method == "median":
        return cv2.medianBlur(gray, 5)
    return cv2.GaussianBlur(gray, (5, 5), 0)
