# Student Engagement Analyzer

This project analyzes student engagement during video sessions by detecting facial emotions in real-time.  
It uses a pre-trained deep learning model (DeepFace) to classify emotions from video frames, helping determine whether a student appears engaged or not.

---

## 📍 Features

- Detects emotions from video using a webcam or uploaded file
- Classifies engagement status: **Engaged** (😃, 😲, 😐) vs **Not Engaged** (😞, 😠, 😢)
- Displays real-time feedback using OpenCV
- User selects video via a Tkinter file dialog

---

## 📍 Installation

### Step 1. Set Python version

If using `pyenv`, set your local version (adjust if needed):

```bash
pyenv local 3.10.13 # Replace 3.10.13 with the Python version shown by `pyenv versions`
```
> Check available versions with:
```
pyenv versions
```
### Step 2. Install Required Python Packages

2-1) Install OpenCV for handling video input and frame processing
```bash
pip install opencv-python
```

2-2) Install DeepFace for emotion detection with pre-trained deep learning models
```bash
pip install deepface
```

2-3) Install tf-keras, required for RetinaFace model compatibility
```bash
pip install tf-keras
```
> tkinter is built into Python on most systems.
> If you're on Linux and it doesn't work, try:
```
sudo apt-get install python3-tk
```
### Step 3. How to Run
From the project directory, run:
```
python student_engagement.py
```
1. Select a video file in the pop-up dialog

2. The analyzer will open a window with real-time emotion and engagement results

3. Press `q` to exit the video window

---

## 📍 Libraries Used
1. `DeepFace`: Emotion detection (VGG-Face model)

2. `OpenCV`: Frame capture and rendering

3. `Tkinter`: File dialog UI

4. `tf-keras`: Required backend for RetinaFace

---

## 📍 Final Report

You can view the full project report here:  [Final Project Report (Google Docs)](https://docs.google.com/document/d/168M0gef6NsiFOpMTsyxWo3XWOMNY-601FMTcBEjiWyk/edit?tab=t.0)

---
## 📍 References
- [DeepFace GitHub](https://github.com/serengil/deepface)
- [OpenCV](https://opencv.org/) 
- [ChatGPT](https://chatgpt.com/)

---

## 📍 Author
- Umulbanin Gulzar

- Yujin Kim
