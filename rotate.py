
########## 좌우로 삐뚤어진 스트립을 벽과 평행하게 조정해주는 코드


import cv2
import numpy as np
from scipy.spatial import distance as dist
import sys
import math


def unit_vector(vector):
   """ Returns the unit vector of the vector.  """
   return vector / np.linalg.norm(vector)

# 두 벡터의 각도를 구해줌
def angle_between(v1, v2):

   v1_u = unit_vector(v1)
   v2_u = unit_vector(v2)
   return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

np.set_printoptions(threshold=sys.maxsize)



# 원본 이미지 불러오기
image = cv2.imread("original.jpg", 1)
image=cv2.resize(image, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)
image = cv2.medianBlur(image,5)
cv2.imshow("Original", image)

blurred = cv2.GaussianBlur(image, (5, 5), 0)


# 이진화
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)


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
print(contours)



contours=np.array(contours)
x=np.argmin(contours[0][:,0][:,0])  #contour중 x좌표가 최소인것의 좌표
y=np.argmin(contours[0][:,0][:,1])  #contour중 y좌표가 최소인것의 좌표

#편의를 위하여, 원점위치를 좌측 상단에서 좌측하단으로 옮김
height, width, channel = image.shape
xx=([0,height]-contours[0][:,0][x])*[-1,1]
yy=([0,height]-contours[0][:,0][y])*[-1,1]

# 두 좌표의 벡터차를 이용하여, 스트립과 x축 사이의 각도를 구함
kk=yy-xx
print(np.linalg.norm(kk,ord=1))
Angle=angle_between(kk,[1,0])*180/np.pi
print(kk)

print(Angle)

x_min=[]
x_max=[]
y_min=[]
y_max=[]

for k in range(0,len(contours)):
    x_min.append(contours[k][:,0][:,0].min())
    x_max.append(contours[k][:,0][:,0].max())
    y_min.append(contours[k][:,0][:,1].min())
    y_max.append(contours[k][:,0][:,1].max())

c_x=np.argmin(x_min)
c_y=np.argmin(y_min)

c_xx=np.argmin(contours[c_x][:,0][:,0])
c_yy=np.argmin(contours[c_y][:,0][:,1])

xx=([0,height]-contours[c_x][:,0][c_xx])*[-1,1]
yy=([0,height]-contours[c_y][:,0][c_yy])*[-1,1]
kk=yy-xx
print(np.linalg.norm(kk,ord=1))
Angle=angle_between(kk,[1,0])*180/np.pi
print(kk)

x_min=np.array(x_min)
x_max=np.array(x_max)
y_min=np.array(y_min)
y_max=np.array(y_max)

x_min=x_min.min()
y_min=y_min.min()
x_max=x_max.max()
y_max=y_max.max()
w=x_max.max()-x_min.min()
h=y_max.max()-y_min.min()

# 스트립이 왼쪽으로 돌아갔는지, 오른쪽으로 돌아갔는지를 구분
if (np.linalg.norm(kk,ord=1))<5:
   Angle=-Angle

else:
   Angle=(90-Angle)


matrix = cv2.getRotationMatrix2D(((x_min+x_max)/2, (y_min+y_max)/2), Angle, 1)
rotated = cv2.warpAffine(image, matrix, (width, height))

cv2.imwrite('rotated_original.png',rotated)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()