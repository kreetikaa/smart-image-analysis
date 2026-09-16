import cv2

def harris_corners(gray):
    gray32 = cv2.convertScaleAbs(gray).astype("float32")
    response = cv2.cornerHarris(gray32, 2, 3, 0.04)
    response = cv2.dilate(response, None)
    return response

def mark_harris_corners(image, response, threshold=0.01):
    result = image.copy()
    result[response > threshold * response.max()] = [0, 0, 255]
    return result
