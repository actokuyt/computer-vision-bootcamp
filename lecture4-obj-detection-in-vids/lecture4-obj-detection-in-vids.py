from ultralytics import YOLO
import cv2


model = YOLO('yolov8n.pt')

cap =cv2.VideoCapture('ppl_vid.mp4')
while True:
    success,frame = cap.read()
    result = model(frame)

    # done = result[0].plot()

    # cv2.imshow("Result", done)


    for i,r in enumerate(result):
        detections = r.boxes.data.tolist()
        names = r.names
        classes = r.boxes.cls.tolist()
    
        for labels,detection in zip(classes,detections):
            label = names[labels]
            x,y,w,h,conf,_ = detection
            cv2.putText(frame,str(label), (int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),1,(cv2.LINE_AA) )
            cv2.rectangle(frame, (int(x),int(y)),(int(w),int(h)),(0,0,255),2)
            
            cv2.imshow("Result", frame)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()