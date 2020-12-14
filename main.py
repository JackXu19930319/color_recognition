import cv2
import numpy as np

img = cv2.imread('test.png', cv2.IMREAD_COLOR)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red_0 = np.array([0, 70, 0])
upper_red_0 = np.array([5, 255, 255])
lower_red_1 = np.array([175, 70, 0])
upper_red_1 = np.array([180, 255, 255])
red_mask0 = cv2.inRange(hsv_img, lower_red_0, upper_red_0)
red_mask1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
red_mask = cv2.bitwise_or(red_mask0, red_mask1)

cv2.imshow("red_mask", red_mask1)
cv2.waitKey(0)