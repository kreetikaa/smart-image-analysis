import cv2

def canny_edges(gray, low=50, high=150):
    return cv2.Canny(gray, low, high)
