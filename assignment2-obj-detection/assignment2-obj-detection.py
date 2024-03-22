from ultralytics import YOLO
import cv2

# Load a model
model = YOLO('computer-vision-bootcamp/venv/yolov8n.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
path = 'computer-vision-bootcamp/assignment2-obj-detection/'
images = [cv2.imread(path + 'cars-img.jpg'), cv2.imread(path + 'off-img.jpg'), cv2.imread(path + 'ppl-img.jpg')]
def resize_images(imgs):
    resized_images = []
    for image in imgs:
        resized_image = cv2.resize(image, (640,416))
        resized_images.append(resized_image)
    return resized_images
resized_images = resize_images(images)

results = model(resized_images, imgsz = (640,416), conf=0.5, classes=[0, 2, 43, 13, 28, 65, 64, 63, 62, 58, 57, 56, 66, 67, 73, 74, 75, 76])  # return a list of Results objects


# Process results list
for i,result in enumerate(results):
    names = result.names
    detections = result.boxes.xyxy.tolist()
    confidences = result.boxes.conf.tolist()
    classes = result.boxes.cls.tolist()
    ppl = 0
    car = 0
    chair = 0
    tv = 0
    for detection, cls, conf in zip(detections, classes, confidences):
        x,y,x2,y2 = detection
        label = names[cls]
        if label == "person":
            ppl += 1
        elif label == "car":
            car += 1
        elif label == "chair":
            chair += 1
        elif label == "tv": 
            tv += 1
        

            
        cv2.rectangle(resized_images[i],(int(x),int(y)),(int(x2),int(y2)), (255,0,0),1)
        cv2.putText(resized_images[i], str(label), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(resized_images[i], str(conf), (int(x), int(y2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)

    object_count = "persons: " + str(ppl) + ", " + "cars: " + str(car) + ", " + "chair: " + str(chair) + ", " + "tv: " + str(tv) 
    cv2.putText(resized_images[i], str(object_count), (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("image"+ str(i), resized_images[i])

cv2.waitKey(0)
