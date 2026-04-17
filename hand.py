import cv2
import mediapipe as mp
import pyautogui as pt
import math

clf = mp.solutions.hands
mp_hand = clf.Hands(max_num_hands=1)
draw_utlis = mp.solutions.drawing_utils
screen_width, screen_height = pt.size()
camera = cv2.VideoCapture(0)
x8=0
y8 =0

while True:
    success, frame = camera.read()
    if not success:
        break
    h, w, c = frame.shape
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = mp_hand.process(frame_rgb)
    hands = output.multi_hand_landmarks
    if hands:
        # drawing landmarks
        for hand in hands:
            draw_utlis.draw_landmarks(frame, hand, clf.HAND_CONNECTIONS)
            # index of landmarks and their landmarks
            for id, lm in enumerate(hand.landmark):
                x, y = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    x8 = screen_width/w*x
                    y8 = screen_height/h*y
                    cv2.circle(frame, (x, y), 15, (255, 255, 0), cv2.FILLED)
                    pt.moveTo(x8, y8)
                if id == 4:
                    x4 = screen_width/w*x    
                    y4 = screen_height/h*y
                    if abs(x4 - x8) < 25 and abs(y4 - y8) < 25:
                        pt.click()
                if id == 12:
                    x12 = screen_width/w*x    
                    y12 = screen_height/h*y
                    if abs(x12 - x4) < 25 and abs(y12 - y4) < 25:
                        pt.rightClick()
                if id == 16:
                    x16 = screen_width/w*x    
                    y16 = screen_height/h*y
                    if abs(x16 - x4) < 25 and abs(y16 - y4) < 25:
                        pt.scroll(250)
                        pt.sleep(0.1)
                if id == 20:
                    x20 = screen_width/w*x    
                    y20 = screen_height/h*y
                    if abs(x20 - x4) < 25 and abs(y20 - y4) < 25:
                        pt.scroll(-250)
                        pt.sleep(0.1)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
        
