import cv2
from deepface import DeepFace
from tkinter import Tk, filedialog

# Open file dialog to select video
Tk().withdraw()
video_path = filedialog.askopenfilename(
    title="Select a video file",
    filetypes=[("Video files", "*.mp4 *.avi *.mov")]
)

# Open video file
cap = cv2.VideoCapture(video_path)

# Create a resizable window
cv2.namedWindow("Student Engagement Analyzer", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Student Engagement Analyzer", 960, 540)

# Start reading frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze the emotion in the frame
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        # Map emotion to engagement status
        engagement = "Engaged" if emotion in ['happy', 'neutral', 'surprise'] else "Not Engaged"
    except:
        emotion = "undetected"
        engagement = "Unknown"

    # Draw emotion and engagement text on the frame
    cv2.putText(frame, f"Emotion: {emotion}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    cv2.putText(frame, f"Engagement: {engagement}", (30, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255) if engagement == "Not Engaged" else (0, 255, 0), 3)

    # Show the frame in the window
    cv2.imshow("Student Engagement Analyzer", frame)

    # Press 'q' to exit
    if cv2.waitKey(9) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
