# Sequence Diagram

```text
User -> Main: provide image path
Main -> Preprocessing: resize/grayscale/blur
Preprocessing -> Edge Detection: blurred image
Main -> Feature Detection: grayscale image
Main -> Shape Detection: image + edges
Main -> Object Detection: image
Main -> Segmentation: image
Modules -> Main: processed results
Main -> Outputs: save result images
Main -> User: report counts/status
```
