# Smart Image Analysis & Object Detection System

A Python and OpenCV computer vision project that demonstrates image preprocessing, edge detection, feature detection, shape/object analysis and K-Means segmentation.

## Features
1. **Image Preprocessing** — grayscale conversion, resizing and Gaussian/median smoothing.
2. **Edge & Feature Detection** — Canny edges and Harris corners.
3. **Shape Detection** — contour approximation for triangles, squares, rectangles and circular/other objects.
4. **Object Analysis** — contour-based bounding boxes and object counting.
5. **Image Segmentation** — K-Means colour segmentation.
6. **Visualization** — saves each processing result as an output image.

## Technologies
- Python 3.10+
- OpenCV
- NumPy
- Matplotlib

## Project Structure
```text
Smart_Image_Analysis/
├── src/
├── tests/
├── data/
├── outputs/
├── diagrams/
├── report/
├── README.md
├── statement.md
└── requirements.txt
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
Put an image inside `data/`, then run:
```bash
python src/main.py --image data/sample.jpg --output outputs
```

For a different number of K-Means clusters:
```bash
python src/main.py --image data/sample.jpg --output outputs --k 4
```

## Testing
```bash
python tests/test_project.py
```
Expected output:
```text
All validation tests passed.
```

## Academic Concepts Demonstrated
Image formation/preprocessing, smoothing, Canny edge detection, Harris corner detection, contours, shape analysis and K-Means segmentation.

## Limitations
The object detector is contour-based rather than a deep-learning detector, so it is intended as an educational computer vision system rather than a production object-recognition model.

## Future Enhancements
- Add YOLO-based object detection.
- Add Hough line/circle visualization.
- Add a desktop GUI.
- Add webcam/live-video processing.
- Add quantitative evaluation on a labelled dataset.
