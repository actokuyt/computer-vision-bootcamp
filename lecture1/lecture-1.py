import cv2


def save_and_display_image(image_name, processed_image):
    # cv2.imwrite("computer-vision-bootcamp/image-processing/"+image_name + ".jpg", processed_image)
    # This saves our processed image to file.
    cv2.imshow(image_name + " window", processed_image)
    # This will open a window on our pc to display our image.


image = cv2.imread("computer-vision-bootcamp/image-processing/image.jpg")
assert image is not None, "file could not be read, check with os.path.exists()"
# This will open the image at the provided path in a numpy format which is how the computer is able to read and
# modify the image.
cv2.imshow("original_image", image)
# This will open a window on our pc to display our image.

resized_image = cv2.resize(image, (200, 200))
# This will resize the opened image to the given size.
save_and_display_image("resized_image", resized_image)

gray_scale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# This will convert our colored image to a gray scale image.
save_and_display_image("resized_image", resized_image)

edged_image = cv2.Canny(gray_scale_image, 100, 200)
# This removes all other parts of the image leaving only the edges of objects in the image
save_and_display_image("edged_image", edged_image)

blurred_image = cv2.GaussianBlur(gray_scale_image, (9, 9), 0)
# This blurs out our image using the provided ksize. the higher the odd number value the blurrier the produced image.
save_and_display_image("blurred_image", blurred_image)

_, threshold_image = cv2.threshold(gray_scale_image, 125, 255, 0)
# Thresholding creates a binary image from grayscale images.
# The idea is to separate an image into regions of interest based on pixel intensity values.
save_and_display_image("threshold_image", threshold_image)

cv2.waitKey(0)
# waitKey provides a delay value for the displayed image, so it remains on screen till we press a button.

cv2.destroyAllWindows()
# Close all  windows opened by cv2
