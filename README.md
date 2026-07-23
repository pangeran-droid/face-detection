# Face Detection using OpenCV

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/Computer%20Vision-Project-orange" />
</p>

This project implements face detection using Python and OpenCV with Haar Cascade Classifier.

The program can detect faces from:

- Image input
- Real-time camera/webcam

## Features

- Face detection from image
- Real-time face detection using webcam
- Draw bounding boxes around detected faces
- Save detection result image

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
├── image/
│   └── faces.jpeg
│
└── output/
    └── face_detection_result.jpg
```

## How to Run

### Face Detection from Image

```bash
python face_detection_image.py
```

### Face Detection using Camera

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

## Detection Parameters

The detection process uses:

```python
detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(40, 40)
)
```

- `scaleFactor` controls the image scale reduction during detection.
- Smaller values improve accuracy but require more computation.
- `minNeighbors` controls detection confidence.
- Higher values reduce false positives but may increase false negatives.

## Example Output

Detected faces will be highlighted with a green rectangle.

![Face Detection Result](output/face_detection_result.jpg)