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

### Step 1. Install and Configure Python 3.10 Environment
**1-1)** Installs Python version 3.10 using Homebrew for use in isolated development environments.
```bash
brew install python@3.10
```
**1-2)** Creates a virtual environment named `.venv` using Python 3.10 in the current directory.
```
python3.10 -m venv .venv
source .venv/bin/activate
```
**1-3)** Upgrades pip to the latest version to ensure smooth and secure package installations.
```
pip install --upgrade pip
```

### Step 2. Install Core Libraries and Dependencies
**2-1)** Installs the `OpenCV` library for image and video processing tasks.
```
pip install opencv-python
```
**2-2)** Installs `TensorFlow version 2.19.0` for machine learning and deep learning development.
```
pip install tensorflow==2.19.0
```
**2-3)** Installs `DeepFace`, a library for face recognition and emotion analysis.
```
pip install deepface==0.0.93
```
**2-4)** Installs the standalone `tf-keras package` to use Keras with TensorFlow backend.
```
pip install tf-keras
```
**2-5)** Installs the `tkinter` GUI toolkit for Python 3.10 to enable graphical user interfaces.
```
brew install python-tk@3.10
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
## 📍 See a quick demo

📽️ [Click here to download the video demo](https://github.com/yujin-k9/CS3120/raw/main/assets/demo.mov)

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
- Yujin Kim (Lead Developer)  
- Umulbanin Gulzar (Developer, Documentation and Testing)


