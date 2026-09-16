import cv2

def detect_shapes(image, edges):
    result = image.copy()
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 500:
            continue

        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        x, y, w, h = cv2.boundingRect(approx)

        if len(approx) == 3:
            name = "Triangle"
        elif len(approx) == 4:
            ratio = w / float(h)
            name = "Square" if 0.90 <= ratio <= 1.10 else "Rectangle"
        else:
            name = "Circle/Object"

        cv2.drawContours(result, [approx], -1, (0, 255, 0), 2)
        cv2.putText(result, name, (x, max(20, y - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        detected += 1

    return result, detected
