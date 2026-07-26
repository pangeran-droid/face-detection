import cv2

# Load the input image
img = cv2.imread('image/faces.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the Haar cascade classifier for face detection
face_cascade_path = 'haarcascade/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(40, 40)
)

print("Detected faces:", len(faces))

# Draw bounding boxes around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the output image
cv2.imwrite("output/face_detection_result.jpg", img)
print("Image saved!")

# Display the result in a window
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()