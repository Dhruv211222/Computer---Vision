# Face and Eye Detection using Haar Cascade Classifiers

## 📌 Project Overview

This project demonstrates **real-time face and eye detection** using OpenCV's **Haar Cascade Classifiers**. The system identifies human faces in images and detects eyes within each detected face region.

Haar Cascade Classifiers are classical machine learning-based feature detectors that use a cascade of trained classifiers to efficiently detect objects in images. This approach is fast, lightweight, and works well for frontal face detection.

---

## 🧠 How It Works

### Face Detection
- Uses the **Haar Cascade Frontal Face Detector** to locate faces in images
- Works exclusively on grayscale images for optimal performance
- Detects multiple faces in a single image

### Eye Detection  
- Applies the **Haar Cascade Eye Detector** within each detected face region (ROI)
- Improves accuracy by searching only within face boundaries
- Marks detected eyes with circular indicators

---

## ⚙️ Technologies Used

- Python
- OpenCV (cv2)
- NumPy
- Matplotlib
- Jupyter Notebook

---

## 📊 Model Components

### Haar Cascade Classifiers

1. **haarcascade_frontalface_default.xml**
   - Pre-trained model for frontal face detection
   - Included with OpenCV library
   - High detection rate for forward-facing faces

2. **haarcascade_eye.xml**
   - Pre-trained model for eye detection
   - Optimized for detecting eyes within face regions
   - Sensitive to eye orientation

### Key Parameters

```python
detectMultiScale(
    image,
    scaleFactor=1.1,      # Image pyramid scale factor
    minNeighbors=5,       # Minimum neighbors for face detection
    minSize=(30, 30)      # Minimum face size in pixels
)
