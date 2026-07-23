import cv2

img = cv2.imread('image/faces.jpeg')

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

path = 'haarcascade/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(40, 40)
)

print("Detected faces:", len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

cv2.imshow(
    "Face Detection",
    img
)

cv2.waitKey(0)
cv2.destroyAllWindows()