import tkinter as tk

import cv2
from PIL import Image, ImageTk

# Load Haar Cascade classifier for face detection
face_cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# Initialize global video capture variables
cap = None
running = False

# Start video capture stream
def start_camera():
    global cap, running

    if not running:
        cap = cv2.VideoCapture(0)
        running = True
        update_frame()


# Read and process frames from the camera feed
def update_frame():
    global cap, running

    if running:
        ret, frame = cap.read()

        if ret:
            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
            )

            # Update the real-time face count on the GUI label
            count_label.config(text=f"Detected Faces: {len(faces)}")

            # Draw bounding boxes around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Convert BGR frame to RGB for Tkinter display
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            camera_label.imgtk = imgtk
            camera_label.configure(image=imgtk)

        window.after(10, update_frame)


# Stop video capture stream
def stop_camera():
    global running, cap

    running = False

    if cap:
        cap.release()
        cap = None

        # Reset the face count label to 0 when the camera stops
        count_label.config(text="Detected Faces: 0")


# Close application safely
def exit_app():
    stop_camera()
    window.destroy()


# GUI Window Setup
window = tk.Tk()
window.title("Face Tracking GUI")
window.geometry("800x650")

# GUI Components
camera_label = tk.Label(window)
camera_label.pack()

count_label = tk.Label(window, text="Detected Faces: 0", font=("Arial", 12, "bold"))
count_label.pack(pady=5)

btn_start = tk.Button(window, text="Start Camera", command=start_camera)
btn_start.pack(pady=5)

btn_stop = tk.Button(window, text="Stop Camera", command=stop_camera)
btn_stop.pack(pady=5)

btn_exit = tk.Button(window, text="Exit", command=exit_app)
btn_exit.pack(pady=5)

# Handle window close button (X) safely
window.protocol("WM_DELETE_WINDOW", exit_app)

window.mainloop()
