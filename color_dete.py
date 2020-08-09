####### 스트립의 색깔분석

import cv2
import numpy as np
from scipy.spatial import distance as dist
import sys

np.set_printoptions(threshold=sys.maxsize)


# Contour 영역 내에 텍스트 쓰기

def setLabel(image, str, contour):

   fontface = cv2.FONT_HERSHEY_SIMPLEX
   scale = 0.6
   thickness = 2

   size = cv2.getTextSize(str, fontface, scale, thickness)
   text_width = size[0][0]
   text_height = size[0][1]

   x, y, width, height = cv2.boundingRect(contour)

   pt = (x + int((width - text_width) / 2), y + int((height + text_height) / 2))
   cv2.putText(image, str, pt, fontface, scale, (255, 255, 255), thickness, 8)



# 컨투어 내부의 색을 평균내서 어느 색인지 체크
def label(image, contour):


   mask = np.zeros(image.shape[:2],dtype='uint8')
   cv2.drawContours(mask, [contour], -1, 255, -1)

   mask = cv2.erode(mask, None, iterations=2)
   mean = cv2.mean(image, mask=mask)[:3]


   minDist = (np.inf, None)



   for (i, row) in enumerate(lab):

       d = dist.euclidean(row[0], mean)

       if d < minDist[0]:
           minDist = (d, i)


   return colorNames[minDist[1]]



# 인식할 색 입력
colors = [[255,255,255],[88,194,225],[170,198,215],[77,190,210],[177,163,135],[59,141,218],
          [179,200,232],[80,198,209],[159,183,171],[49,178,227],
          [77,197,197],[192,208,225],[186,208,226],[168,180,222],[81,190,192],[124,176,169],[68,186,203],
          [26,89,87],[74,122,186],[90,137,205],[37,45,134],[73,127,138],[26,80,121],[30,69,71],
          [34,60,47],[78,119,204],[45,44,110],[95,146,48],[9,67,126],[74,70,65],
          [75,102,222],[96,128,117],[4,81,156]
          ]
colorNames = ['white','1-1','2-1','3-1','4-1','5-1',
              '4-2','5-2','6-2','7-2',
              '1-3','2-3','3-3','4-3','5-3','6-3','7-3',
              '1-4','2-4','3-4','4-4','5-4','6-4','7-4',
              '1-5','2-5,3-5','4-5','5-5','6-5','7-5',
              '3-6','5-6','6-6']



lab = np.zeros((len(colors), 1, 3),dtype='uint8')

for i in range(len(colors)):
   lab[i] = colors[i]

lab = cv2.cvtColor(lab, cv2.COLOR_BGR2LAB)




# 원본 이미지 불러오기
image = cv2.imread("U10.png", 1)
image = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)
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





contours=np.array(contours)


# 컨투어의 x, y 좌표, width, height 구함
x=contours[0][:,0][:,0].min()
y=contours[0][:,0][:,1].min()
w=contours[0][:,0][:,0].max()-contours[0][:,0][:,0].min()
h=contours[0][:,0][:,1].max()-contours[0][:,0][:,1].min()



cropped=image[y: y + h, x: x + w]
cv2.imwrite("U1313.png", cropped)
cv2.imshow("image11111", cropped)

cv2.waitKey(0)


###############################################
image = cv2.imread("U1313.png", 1)


blurred = cv2.GaussianBlur(image, (5, 5), 0)


# 이진화
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
print(gray)

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

# 컨투어 별로 체크
for contour in contours:

      cv2.imshow("Image", image)
      cv2.waitKey(0)

      # 컨투어를 그림
      cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)


      # 컨투어 내부에 검출된 색을 표시
      color_text = label(img_lab, contour)
      setLabel(image, color_text, contour)
      print(color_text)


cv2.imshow("Image", image)
cv2.waitKey(0)