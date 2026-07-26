import cv2

# Read image
img = cv2.imread("image/faces.jpeg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade classifiers for face and eye detection
face_cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
eye_cascade_path = "haarcascade/haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Face detection
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

print("Detected faces:", len(faces))

total_eyes = 0

# Process each detected face
for (x, y, w, h) in faces:

    # Region of Interest (ROI) for face
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

    # Eye detection within the face area
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=8)

    total_eyes += len(eyes)

    # Draw circles around detected eyes
    for (ex, ey, ew, eh) in eyes:
        center = (ex + ew // 2, ey + eh // 2)
        radius = int((ew + eh) / 4)

        cv2.circle(roi_color, center, radius, (255, 0, 0), 2)

print("Detected eyes:", total_eyes)

# Save the output image
cv2.imwrite("output/eye_detection_result.jpg", img)
print("Image saved!")

# Display result
cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
