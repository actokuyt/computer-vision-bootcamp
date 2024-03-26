from  ultralytics import  YOLO
import cv2

model = YOLO("yolov8n.pt")
image = cv2.imread("ppl-img.jpg")

results = model(image)




for i,r in enumerate(results):
    detection = r.boxes.data.tolist()
    names = r.names
    classes = r.boxes.cls.tolist()

    for labels,detection in zip(classes,detection):
        label = names[labels]
        x,y,w,h,conf,_ = detection


        cv2.putText(image, str(label), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(image, str(conf), (int(x), int(h)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)

        cv2.rectangle(image,(int(x),int(y)),(int(w),int(h)), (255,0,0),1)

    cv2.imshow("image",image)
    cv2.waitKey(0)