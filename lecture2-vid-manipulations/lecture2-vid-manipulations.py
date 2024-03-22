import cv2 as cv 


cap = cv.VideoCapture("computer-vision-bootcamp/lecture2/bgr.mp4")

fourcc = cv.VideoWriter_fourcc(*'mp4v')
output = cv.VideoWriter('computer-vision-bootcamp/lecture2/out.mp4',fourcc,30,(400,200))

while cap.isOpened:
    ret, frame  = cap.read()

    if not ret:
        cap = cv.VideoCapture("computer-vision-bootcamp/assignment1/bgr.mp4")
        continue

    frame = cv.resize(frame,(400,200))
    vid_Gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur_Vid = cv.GaussianBlur(frame,(9,9),0)
    vidBlur = cv.blur(frame,(7,7))
    _,thresh_frame = cv.threshold(vid_Gray,50,150,cv.THRESH_BINARY)
    


    output.write(blur_Vid)

    cv.imshow('frame',frame)
    cv.imshow('frame_GRAY',vid_Gray)
    cv.imshow('frame_BLUR',vidBlur)
    cv.imshow('frame_THRESH',thresh_frame)
    cv.imshow('frame',frame)

    k = cv.waitKey(1) & 0xFF

    if k == 27:
        break

cap.release()
output.release()
cv.destroyAllWindows()