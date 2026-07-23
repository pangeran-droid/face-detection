# Face Detection using OpenCV

This project implements face detection using Python and OpenCV with Haar Cascade Classifier.

The program can detect faces from:

- Image input
- Real-time camera/webcam

## Features

- Face detection from image
- Real-time face detection using webcam
- Draw bounding boxes around detected faces

## Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

## Project Structure

```text
face_detection/
│
├── face_detection_image.py
├── face_detection_camera.py
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
└── image/
    └── faces.jpeg
```

## How to Run

### Face Detection from Image

Run:

```bash
python face_detection_image.py
```

### Face Detection using Camera

Run:

```bash
python face_detection_camera.py
```

Press `ESC` to exit the camera window.

## Method

This project uses:

- Grayscale conversion
- Haar Cascade Classifier
- Multi-scale face detection
- Bounding box visualization

## Example Output

Detected faces will be highlighted with a green rectangle.
