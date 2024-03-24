########Pose detection#######
import cv2
from cvzone.PoseModule import PoseDetector
cap = cv2.VideoCapture(1)
my_detector = PoseDetector()
while 1:
  _,frame = cap.read()
  frame = my_detector.findPose(frame)
  lmlist, bbox = my_detector.findPosition(frame,bboxWithHands=False)
  # print(lmlist)
  nose = lmlist[0]
  nx,ny,_ = nose
  print(nose)
  cv2.circle(frame,(nx,ny),10,(0,0,255),-1)
  cv2.imshow('frame',frame)
  key = cv2.waitKey(1)
  if key == 27:
    break
cap.release()
cv2.destroyAllWindows()





#######FACE DETECTION#######
import cv2
from cvzone.FaceDetectionModule import FaceDetector
cap = cv2.VideoCapture(1)
my_detector = FaceDetector()
while 1:
  _,frame = cap.read()
  frame,results = my_detector.findFaces(frame)
  # print(results)
  for parameter in results:
    bbox = parameter['bbox']
    center = parameter['center']
    score = parameter['score']
    print(bbox,center , sep='  ')
    cv2.circle(frame,center,10,(0,0,255),-1)
  cv2.imshow('frame',frame)
  key = cv2.waitKey(1)
  if key == 27:
    break
cap.release()
cv2.destroyAllWindows()