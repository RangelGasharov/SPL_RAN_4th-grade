import cv2

img = cv2.imread('images/road.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("img", img)
cv2.imshow("img_rgb", img_rgb)
cv2.waitKey(0)
