import cv2

def save_image(path, image):
    if not cv2.imwrite(str(path), image):
        raise IOError(f"Could not save image: {path}")
