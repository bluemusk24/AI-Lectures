import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

#cap = cv2.VideoCapture(0) 
cap = cv2.VideoCapture('shadow_crowd.mp4')   # captures from camera. Video Path can be added instead of zero

while True:
    ret, frame = cap.read()
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow('Live Camera Feed', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # press q to quit
        break

cap.release()
cv2.destroyAllWindows()