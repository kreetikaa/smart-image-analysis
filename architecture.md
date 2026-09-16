# System Architecture

```text
Input Image
    |
    v
Preprocessing
    |
    +--> Grayscale --> Blur --> Canny Edge Detection
    |                         |
    |                         +--> Shape Detection
    |
    +--> Harris Corner Detection
    |
    +--> Contour Object Detection
    |
    +--> K-Means Segmentation
    |
    v
Saved Visual Results
```
