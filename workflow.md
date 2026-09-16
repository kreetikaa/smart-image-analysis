# Workflow

```text
Start
  |
Read Image
  |
Validate Image
  |
Resize / Grayscale / Blur
  |
  +--> Canny Edges
  +--> Harris Corners
  +--> Shape Detection
  +--> Object Detection
  +--> K-Means Segmentation
  |
Save Results
  |
Display Counts / Status
  |
End
```
