# Component/Class Diagram

```text
+------------------+
|      main.py     |
+--------+---------+
         |
 +-------+-------------------------------+
 |       |          |        |           |
 v       v          v        v           v
Preprocess  Edge   Feature  Shape      Object
            Detect  Detect   Detect     Detect
 |
 v
Segmentation
 |
 v
Visualization
```
