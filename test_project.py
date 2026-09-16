import sys
from pathlib import Path
import numpy as np
import cv2

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from preprocessing import to_grayscale, blur_image
from edge_detection import canny_edges
from segmentation import kmeans_segment

img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(img, (20, 20), (80, 80), (255, 255, 255), -1)

gray = to_grayscale(img)
assert gray.shape == (100, 100)

blur = blur_image(gray)
assert blur.shape == gray.shape

edges = canny_edges(blur)
assert edges.shape == gray.shape

segmented = kmeans_segment(img, 2)
assert segmented.shape == img.shape

print("All validation tests passed.")
