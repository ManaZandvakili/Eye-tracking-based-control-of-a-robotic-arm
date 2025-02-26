import cv2
import numpy as np
import dlib
from math import hypot
import math
import pyautogui
from imutils import face_utils
import imutils
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from datetime import datetime,timedelta
pyautogui.FAILSAFE = False
Scroll = False
pTime = 0
# variables for frame rate
frame_counter = 0
start_time = time.time()
FPS = 0
present_time = datetime.now()
print(present_time)
#To load the camera, 0 is for when you only have one camera
cap = cv2.VideoCapture(0) 
#First load the face detector, used in the frames to detect faces
detector = dlib.get_frontal_face_detector()      
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# to detect the landmarks
font = cv2.FONT_HERSHEY_SIMPLEX
def middlepoint(n1, n2):
    #def for Find a midpoint between 37, 38 and 40, 41 pixels cannot be float
    return int((n1.x + n2.x)/2), int((n1.y + n2.y)/2)  
def eye_aspect_ratio(eye):
    # Compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    # Compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = np.linalg.norm(eye[0] - eye[3])
    # Compute the eye aspect ratio
    ear = (A + B)/(2.0 *C)
   # Return the eye aspect ratio
    return ear
def blinking_ratio(eye_points, face_landmarks):
    eye_left = (face_landmarks.part(eye_points[0]).x, face_landmarks.part(eye_points[0]).y)
    eye_right = (face_landmarks.part(eye_points[3]).x, face_landmarks.part(eye_points[3]).y)
    eye_top = middlepoint(face_landmarks.part(eye_points[1]), face_landmarks.part(eye_points[2]))
    eye_bottom = middlepoint(face_landmarks.part(eye_points[5]), face_landmarks.part(eye_points[4]))
    hLine = cv2.line(frame, eye_left, eye_right, (0, 255, 0), 2)
    vLine = cv2.line(frame, eye_top, eye_bottom, (0, 255, 0), 2)
    cv2.rectangle(frame, (eye_left[0] - 10, eye_bottom[1] - 20), (eye_right[0] + 10, eye_top[1] + 20), (0, 255, 255), 2)
    #hypot() method returns the Euclidean norm of horizental line
    hor_lenght = hypot((eye_left[0]) - eye_right[0], (eye_left[1] - eye_right[1])) 
    ver_lenght = hypot((eye_top[0]) - eye_bottom[0], (eye_bottom[1] - eye_top[1]))
    ratio = ver_lenght/hor_lenght
    return ratio
def gaze_ratio_LR(eye_points,facial_landmarks):
    eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                           (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                           (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                           (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                           (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                           (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)],np.int32)
    # SELECTING ONLY THE EYE FROM FACE
    h,w,_=frame.shape
    mask=np.zeros((h, w), np.uint8) #creating a black screen
    cv2.polylines(mask, [eye_region], True, 255, 2)
    cv2.fillPoly(mask, [eye_region], 255) # filling the eye polygon with white color
    left_eye = cv2.bitwise_and(gray, gray, mask=mask) # need to see what it does
    
    min_x = np.min(eye_region[:, 0])
    max_x = np.max(eye_region[:, 0])
    min_y = np.min(eye_region[:, 1])
    max_y = np.max(eye_region[:, 1])

    eye = frame[min_y: max_y, min_x: max_x] # selecting the rectangular region with eye only
    gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY) # making gray scale
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255,cv2.THRESH_BINARY) # creating a threshold
    h, w = threshold_eye.shape
    left_Threshold = threshold_eye[0:h, 0:int(w / 2)] # left part of threshold_eye window
    left_White = cv2.countNonZero(left_Threshold) # zero mean black so non zero mean white
    
    right_Threshold = threshold_eye[0:h, int(w / 2):w] # right part of threshold_eye window
    right_White = cv2.countNonZero(right_Threshold)
    if left_White == 0:
        gaze_ratio = 1 
    elif right_White == 0:
        gaze_ratio = 3
    else:
        gaze_ratio = left_White / right_White
    return gaze_ratio      
                                                                    
def gaze_ratio_UD(eye_points,facial_landmarks):
    eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                           (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                           (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                           (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                           (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                           (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)],np.int32)
    # SELECTING ONLY THE EYE FROM FACE              
    h,w,_=frame.shape
    mask = np.zeros((h, w), np.uint8) # creating a black screen
    cv2.polylines(mask, [eye_region], True, 255, 2)
    cv2.fillPoly(mask, [eye_region], 255) # filling the eye polygon with white color
    left_eye = cv2.bitwise_and(gray, gray, mask=mask) # need to see what it does   
                                                                    
    min_x = np.min(eye_region[:, 0])
    max_x = np.max(eye_region[:, 0])
    min_y = np.min(eye_region[:, 1])
    max_y = np.max(eye_region[:, 1])      
                                                                    
    eye = frame[min_y: max_y, min_x: max_x] # selecting the rectangular region with eye only,show the rectangle on the frame
    gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY) # making gray scale
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY) # creating a threshold dont know exactly what it mean
    h, w = threshold_eye.shape
    down_Threshold = threshold_eye[0:int(h/2), 0:w] # bottom part of threshold_eye window
    down_White = cv2.countNonZero(down_Threshold) # zero mean black non zero mean white
    
    up_Threshold = threshold_eye[int(h/2):h, 0:w] # upper part of threshold_eye window
    up_White = cv2.countNonZero(up_Threshold)
    
    if up_White == 0:
        gaze_ratio = 0.00001
    elif down_White == 0:
        gaze_ratio = 30000
    else:
        gaze_ratio = up_White / down_White
    return gaze_ratio

def eye_movement_detection_LR(avg_blink_ratio):
                                                  
    if avg_blink_ratio<= 0.8: 
        return "Left"
    elif avg_blink_ratio> 0.8 and avg_blink_ratio<=1.1:
        return "Center"
    else:
        return "Right"
                                                                    
                                                                    
def eye_movement_detection_UD(avg_blink_ratio):
                                                  
    if avg_blink_ratio>= 1.4 and avg_blink_ratio<= 3: 
        return "Down"
    elif avg_blink_ratio> 3 and avg_blink_ratio<=4:
        return "Center"
    else:
        return "Up"
                                                                    
                                                                            
while True: 
    frame_counter += 1
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
                                                                    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime  
                                                                    
    #loop over all the face detections and apply the predictor 
    for face in faces:     
                                                                    
        face_x, face_y = face.left(), face.top()
        face_x1, face_y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (face_x, face_y), (face_x1, face_y1), (0, 0, 255), 2) 
        landmarks = predictor(gray, face) # the points on the face
                                                                    
    # BLINK DETECTION
                                                                    
        right_ratio = blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        left_ratio = blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        net_blink_ratio = (right_ratio + left_ratio)/2.0   
                                                                    
                                                            
        if net_blink_ratio >= 5.7:
                                                                    
            Scroll = not Scroll
            if not Scroll:
                cv2.putText(frame, "Scroll Enabled", (250, 50), font, 1, (255, 0, 0), 3) 
            if Scroll:
                cv2.putText(frame, "Scroll Disabled", (250, 50), font, 1, (255, 0, 0), 3)
                
                
        elif net_blink_ratio < 0.2:
                cv2.putText(frame, "Blink", (250, 50), font, 1, (255, 0, 0), 3)    #Write a text on the frame,
                pyautogui.click()
            
    # GAZE DETECTION 
        
        gaze_ratio_righteye_LR = gaze_ratio_LR([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_righteye_UD = gaze_ratio_UD([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_lefteye_LR = gaze_ratio_LR([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio_lefteye_UD = gaze_ratio_UD([42, 43, 44, 45, 46, 47], landmarks)
         
        net_gaze_ratio_LR = (gaze_ratio_lefteye_LR + gaze_ratio_righteye_LR)/2.0
        net_gaze_ratio_UD = (gaze_ratio_lefteye_UD + gaze_ratio_righteye_UD)/2.0  
                                                              
        if net_gaze_ratio_LR <= 0.8:
            cv2.putText(frame, "Gaze: Left", (400,50), font, 1, (0, 0, 255), 2)
        elif net_gaze_ratio_LR > 0.8 and net_gaze_ratio_LR <= 1.1:
            cv2.putText(frame, "CENTER", (400, 50), font, 1, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Gaze: Right", (400, 50), font, 1, (0, 0, 255), 2)
        if net_gaze_ratio_UD >= 1.4 and net_gaze_ratio_UD <= 3:
            cv2.putText(frame, "Gaze: Up", (40, 50), font, 1, (0, 0, 255), 2)
        elif net_gaze_ratio_UD > 3 and net_gaze_ratio_UD <= 4:
            cv2.putText(frame, "CENTER", (40, 50), font, 1, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Gaze: Down", (40, 50), font, 1, (0, 0, 255), 2)
        if eye_movement_detection_LR(net_gaze_ratio_LR) == "Right":
            pyautogui.move(20, 0)
        if eye_movement_detection_LR(net_gaze_ratio_LR) == "Left":
            pyautogui.move(-20, 0)
        if eye_movement_detection_UD(net_gaze_ratio_UD) == "Up":
            pyautogui.move(0, 10)
        if eye_movement_detection_UD(net_gaze_ratio_UD) == "Down":
            pyautogui.move(0, -10)
                                                                    
                        
        # calculating the frame rate
        Sec = time.time() - start_time 
        FPS = frame_counter/Sec 
        cv2.putText(frame, f'FPS:{int(FPS)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                                                                    
                                                                    
                                                                    
        cv2.imshow("FINAL",frame)   #To show the frame
    # if q is pressed on keyboard: quit #Create a Condition, the input is ASCII
    key = cv2.waitKey(1)
    if key == ord('q'):
        break      
                                                                    
cap.release()
cv2.destroyAllWindows()     #To close all windows 
