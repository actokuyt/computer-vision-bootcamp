import numpy as np
import cv2 as cv
 

img = cv.imread('computer-vision-bootcamp/assignment1/sudoku.png')
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols,ch = img.shape


# Scaling
scaled_img = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
 
#OR
 
height, width = img.shape[:2]
scaled_img = cv.resize(img,(3*width, 2*height), interpolation = cv.INTER_CUBIC)


# Translation
M = np.float32([[1,0,100],[0,1,50]])
translated_img = cv.warpAffine(img,M,(cols,rows))

# Rotation
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
rotated_img = cv.warpAffine(img,M,(cols,rows))


# Affine Transformed
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
 
M = cv.getAffineTransform(pts1,pts2)
 
affine_transformed_img = cv.warpAffine(img,M,(cols,rows))


# Perspective Transformed 
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
 
M = cv.getPerspectiveTransform(pts1,pts2)
 
perspective_transformed_img = cv.warpPerspective(img,M,(300,300))




cv.imshow("Original", img )
cv.imshow("Scaled Image", scaled_img)
cv.imshow('Translated Image',translated_img)
cv.imshow("Rotated Image", rotated_img)
cv.imshow("Affine Transformed Image", affine_transformed_img)
cv.imshow("Perspective Transformed Image", perspective_transformed_img)
cv.waitKey(0)
cv.destroyAllWindows()