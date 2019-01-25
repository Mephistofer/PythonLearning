import cv2
import numpy as np
image = cv2.imread("F:\\OpenCVTestData\\Image\\Image1.jpg")

# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Over theClouds", image)

# cv2.imshow("Over theClouds - gray", gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
