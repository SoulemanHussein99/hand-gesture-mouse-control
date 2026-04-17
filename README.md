# Hand Gesture Mouse Control (MediaPipe + OpenCV)

A real-time computer vision system that allows controlling the mouse using hand gestures.  
Built using MediaPipe for hand tracking and OpenCV for video processing.

---

## Features

- Move mouse using index finger 
- Left click using thumb + index finger
- Right click using middle finger gesture
- Scroll up/down using hand gestures
- Real-time hand tracking
- Smooth interaction without physical mouse

---

## How It Works

1. Webcam captures live video  
2. MediaPipe detects hand landmarks (21 points)  
3. Specific finger positions are tracked  
4. Gestures are interpreted into actions:
   - Cursor movement  
   - Click  
   - Right click  
   - Scroll  
5. PyAutoGUI executes system commands  

---

## Controls (Gestures)

- Index finger (ID 8) → Move cursor  
- Thumb (4) + Index (8) → Left Click  
- Thumb (4) + Middle (12) → Right Click  
- Thumb (4) + Ring (16) → Scroll Up  
- Thumb (4) + Pinky (20) → Scroll Down  

---

## Technologies Used

- Python 
- OpenCV
- MediaPipe (Hand Tracking)
- PyAutoGUI
