import cv2

img=cv2.imread("image (1).jpg")
img=cv2.resize(img, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Strip",img)

cv2.waitKey(0)