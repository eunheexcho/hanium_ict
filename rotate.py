import cv2
import numpy as np
from scipy.spatial import distance as dist
import sys
import math


def unit_vector(vector):
   """ Returns the unit vector of the vector.  """
   return vector / np.linalg.norm(vector)


def angle_between(v1, v2):

   v1_u = unit_vector(v1)
   v2_u = unit_vector(v2)
   return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

np.set_printoptions(threshold=sys.maxsize)



# 원본 이미지 불러오기
image = cv2.imread("U2222.png", 1)
cv2.imshow("Original", image)

blurred = cv2.GaussianBlur(image, (5, 5), 0)


# 이진화
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)


cv2.imshow('gray',gray)
# 색검출할 색공간으로 LAB사용
img_lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

thresh = cv2.erode(thresh, None, iterations=2)
cv2.imshow("Thresh", thresh)


# 컨투어 검출
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# 컨투어 리스트가 OpenCV 버전에 따라 차이있기 때문에 추가
if len(contours) == 2:
   contours = contours[0]

elif len(contours) == 3:
   contours = contours[1]



# contours = contours.astype("float")
#
# contours = contours.astype("int")



print(contours)


for contour in contours:
   x, y, w, h = cv2.boundingRect(contour)
   print(x,y,w,h)

# cropped = image[y:y+h, x:x+w]
cropped=image[y: y + h, x: x + w]
cv2.imwrite("U1313.png", cropped)
cv2.imshow("image11111", cropped)

height, width, channel = image.shape

contours=np.array(contours)
x=np.argmin(contours[0][:,0][:,0])
y=np.argmin(contours[0][:,0][:,1])
print(x)
print(y)
xx=([0,height]-contours[0][:,0][x])*[-1,1]
yy=([0,height]-contours[0][:,0][y])*[-1,1]
print(xx)
print(yy)
kk=yy-xx
print(np.linalg.norm(kk,ord=1))
Angle=angle_between(kk,[1,0])*180/np.pi

print(Angle)

if (np.linalg.norm(kk,ord=1))<100:
   Angle=-Angle

else:
   Angle=90-Angle


matrix = cv2.getRotationMatrix2D((width/2, height/2), Angle, 0.8)
rotated = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()