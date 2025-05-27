

# Facial Landmarks Detection with OpenCV, MediaPipe, and Python

This project demonstrates real-time facial landmarks detection using Python with OpenCV and MediaPipe. It detects key points on a person's face such as eyes, nose, mouth, and facial contours, providing a foundation for facial analysis, emotion detection, filters, and AR applications.

## Demo

![Demo GIF](demo.gif) *(Optional – Add a screen recording if available)*

---

## Features

- Real-time webcam-based facial landmark detection
- Tracks 468 facial landmarks using MediaPipe Face Mesh
- Annotates detected landmarks with OpenCV

---

## Libraries Used

- **[OpenCV](https://pypi.org/project/opencv-python/)** - for real-time video capture and image processing.
- **[MediaPipe](https://pypi.org/project/mediapipe/)** - for facial landmark detection.
- **[NumPy](https://pypi.org/project/numpy/)** - for numerical operations (optional but commonly used).
- **Python 3.x**

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RandomRohit-hub/Facial-Landmarks-Detection-with-Opencv-mediappipe-and-python.git
   cd Facial-Landmarks-Detection-with-Opencv-mediappipe-and-python

2. Create virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


3. Install required libraries:

pip install -r requirements.txt

If requirements.txt is not available, manually install:

pip install opencv-python mediapipe




---

Usage

1. Run the main script:

python main.py


2. Your webcam will open and start detecting facial landmarks.


3. Press 'q' to exit the window.




---

How It Works

Uses OpenCV to access the webcam and draw visual landmarks.

MediaPipe's Face Mesh module detects and tracks 468 facial landmarks in real-time.

The detected landmarks are drawn using cv2.circle or cv2.polylines.



---

Folder Structure

Facial-Landmarks-Detection/
├── main.py                 # Main script
├── README.md               # Project documentation
└── demo.gif (optional)     # Example demo


---

Future Improvements

Add support for multiple faces

Save landmark coordinates for further processing

Integrate with filters or emotion recognition



---



