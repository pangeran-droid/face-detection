import cv2

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Load the Haar cascade classifier for face detection
face_cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)

while True:
    # Read frame from the camera
    ret, frame = cap.read()

    # Exit loop if frame is not retrieved
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    print(f"\rDetected faces: {len(faces)}", end="")

    # Draw bounding boxes around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Face Camera Detection", frame)

    # Press 'ESC' key to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
