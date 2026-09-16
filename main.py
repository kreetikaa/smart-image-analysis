import argparse
from pathlib import Path
import cv2

from preprocessing import to_grayscale, blur_image, resize_image
from edge_detection import canny_edges
from feature_detection import harris_corners, mark_harris_corners
from shape_detection import detect_shapes
from object_detection import detect_objects_by_contours
from segmentation import kmeans_segment
from visualization import save_image

def process(image_path, output_dir, k=3):
    output_dir.mkdir(parents=True, exist_ok=True)
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Image not found or unreadable: {image_path}")

    image = resize_image(image)
    gray = to_grayscale(image)
    blur = blur_image(gray)
    edges = canny_edges(blur)

    corners = harris_corners(gray)
    corner_img = mark_harris_corners(image, corners)

    shapes, shape_count = detect_shapes(image, edges)
    objects, object_count = detect_objects_by_contours(image)
    segmented = kmeans_segment(image, k)

    save_image(output_dir / "01_grayscale.jpg", gray)
    save_image(output_dir / "02_blurred.jpg", blur)
    save_image(output_dir / "03_edges.jpg", edges)
    save_image(output_dir / "04_harris_corners.jpg", corner_img)
    save_image(output_dir / "05_shapes.jpg", shapes)
    save_image(output_dir / "06_objects.jpg", objects)
    save_image(output_dir / "07_kmeans_segmentation.jpg", segmented)

    print("Processing completed.")
    print(f"Shapes detected: {shape_count}")
    print(f"Objects detected: {object_count}")
    print(f"Results saved to: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart Image Analysis using OpenCV")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument("--k", type=int, default=3, help="K for K-Means segmentation")
    args = parser.parse_args()

    process(Path(args.image), Path(args.output), args.k)
