####### 스트립의 색깔분석

import cv2
import numpy as np
from scipy.spatial import distance as dist
import sys

np.set_printoptions(threshold=sys.maxsize)


def Health_detect(x):
    if x.endswith('1'):
        return 'negative'
    elif x.endswith('2'):
        return 'negative'
    elif x.endswith('3'):
        return 'positive'
    elif x.endswith('4'):
        return 'positive'
    elif x.endswith('5'):
        return 'positive'
    elif x.endswith('6'):
        return 'positive'
    else:
        return 'positive'

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
def label(image, contour,lab,colorNames):

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
colors = [[255,255,255],[0,0,0],[88,194,225],[170,198,215],[77,190,210],[177,163,135],[59,141,218],
          [179,200,232],[80,198,209],[159,183,171],[49,178,227],
          [77,197,197],[192,208,225],[186,208,226],[168,180,222],[81,190,192],[124,176,169],[68,186,203],
          [26,89,87],[74,122,186],[90,137,205],[37,45,134],[73,127,138],[26,80,121],[30,69,71],
          [34,60,47],[78,119,204],[45,44,110],[95,146,48],[9,67,126],[74,70,65],
          [75,102,222],[96,128,117],[4,81,156]
          ]
colorNames = ['white','black','1-1','2-1','3-1','4-1','5-1',
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
image = cv2.imread("rotated_original.png", 1)

#cv2.imshow("glucose_14cm.png", image)

blurred = cv2.GaussianBlur(image, (5, 5), 0)


# 이진화
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)


#cv2.imshow('gray',gray)
# 색검출할 색공간으로 LAB사용
img_lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

thresh = cv2.erode(thresh, None, iterations=2)
#cv2.imshow("Thresh", thresh)


# 컨투어 검출
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# 컨투어 리스트가 OpenCV 버전에 따라 차이있기 때문에 추가
if len(contours) == 2:
   contours = contours[0]

elif len(contours) == 3:
   contours = contours[1]





contours=np.array(contours)



# 컨투어의 x, y 좌표, width, height 구함
x_min=[]
x_max=[]
y_min=[]
y_max=[]

for k in range(0,len(contours)):
    x_min.append(contours[k][:,0][:,0].min())
    x_max.append(contours[k][:,0][:,0].max())
    y_min.append(contours[k][:,0][:,1].min())
    y_max.append(contours[k][:,0][:,1].max())

x_min=np.array(x_min)
x_max=np.array(x_max)
y_min=np.array(y_min)
y_max=np.array(y_max)

x=x_min.min()
y=y_min.min()
w=x_max.max()-x_min.min()
h=y_max.max()-y_min.min()



cropped=image[y: y + h, x: x + w]





cv2.imwrite("U1313.png", cropped)
cv2.imshow("Cropped Image", cropped)


##################################################################################################################################
image = cv2.imread("U1313.png", 1)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
h, w, c = image.shape








first=blurred[round(0.6*w):round(1.4*w), round(0.2*w):round(0.8*w)]

cv2.imshow('first',first)

# cv2.imshow('gray',gray)






contours=[
    [[0,0]],
    [[0,round(0.8*w)]],
    [[round(0.6*w),round(0.8*w)]],
    [[round(0.6*w),0]]
]
contours=np.array(contours)

def colorDetection(number):
    color_text=label(number,)

first_color=[[255,255,255],[0,0,0],[88,194,225],[77,197,197],[26,89,87],[34,60,47]]


first_color_hsv = np.zeros((len(first_color), 1, 3),dtype='uint8')
for i in range(len(first_color)):
   first_color_hsv[i] = first_color[i]

first_color_hsv = cv2.cvtColor(first_color_hsv, cv2.COLOR_BGR2HSV)
first_color_name=['white','black','1-1','1-3','1-4','1-5']

first = cv2.cvtColor(first, cv2.COLOR_BGR2HSV)
first_color_text= label(first,contours,first_color,first_color_name)


# second
second_color=[[255,255,255],[0,0,0],[170,198,215],[192,208,225],[74,122,186],[78,119,204]]
second_color_name=['white',[0,0,0],'2-1','2-3','2-4','2-5']

second_color_hsv = np.zeros((len(second_color), 1, 3),dtype='uint8')
for i in range(len(second_color)):
   second_color_hsv[i] = second_color[i]

second_color_hsv = cv2.cvtColor(second_color_hsv, cv2.COLOR_BGR2HSV)
second=blurred[round(2.1*w):round(2.9*w), round(0.2*w):round(0.8*w)]
cv2.imshow('second',second)
second = cv2.cvtColor(second, cv2.COLOR_BGR2HSV)


second_color_text= label(second,contours,second_color_hsv,second_color_name)


#############Third####################
third_color=[[255,255,255],[0,0,0],[195,201,214],[186,208,226],[90,137,205],[78,119,204],[75,102,222]]
third_color_name=['white','black','3-1','3-3','3-4','3-5','3-6']

third_color_hsv = np.zeros((len(third_color), 1, 3),dtype='uint8')
for i in range(len(third_color)):
   third_color_hsv[i] = third_color[i]

third_color_hsv = cv2.cvtColor(third_color_hsv, cv2.COLOR_BGR2HSV)
third=blurred[round(3.6*w):round(4.4*w), round(0.2*w):round(0.8*w)]
cv2.imshow('third',third)
third = cv2.cvtColor(third, cv2.COLOR_BGR2HSV)


third_color_text= label(third,contours,third_color_hsv,third_color_name)


##############Fourth####################
fourth_color=[[255,255,255],[0,0,0],[195,201,214],[179,200,232],[168,180,222],[37,45,134],[45,44,110]]
fourth_color_name=['white','black','4-1','4-2','4-3','4-4','4-5']

fourth_color_hsv = np.zeros((len(fourth_color), 1, 3),dtype='uint8')
for i in range(len(fourth_color)):
   fourth_color_hsv[i] = fourth_color[i]

fourth_color_hsv = cv2.cvtColor(fourth_color_hsv, cv2.COLOR_BGR2HSV)
fourth=blurred[round(5.1*w):round(5.9*w), round(0.2*w):round(0.8*w)]
cv2.imshow('fourth',fourth)
fourth = cv2.cvtColor(fourth, cv2.COLOR_BGR2HSV)


fourth_color_text= label(fourth,contours,fourth_color_hsv,fourth_color_name)



############Fifth#################33
fifth_color=[[255,255,255],[0,0,0],[130,170,130],[130,182,198],[97,207,211],[125,172,150],[140,173,142],[158,161,120]]
fifth_color_name=['white','black','5-1','5-2','5-3','5-4','5-5','5-6']

fifth_color_hsv = np.zeros((len(fifth_color), 1, 3),dtype='uint8')
for i in range(len(fifth_color)):
   fifth_color_hsv[i] = fifth_color[i]

fifth_color_hsv = cv2.cvtColor(fifth_color_hsv, cv2.COLOR_BGR2HSV)
fifth=blurred[round(6.6*w):round(7.4*w), round(0.2*w):round(0.8*w)]
cv2.imshow('fifth',fifth)
fifth = cv2.cvtColor(fifth, cv2.COLOR_BGR2HSV)


fifth_color_text= label(fifth,contours,fifth_color_hsv,fifth_color_name)




###############Sixth#####################

sixth_color=[[255,255,255],[0,0,0],[149,130,147],[145,138,153],[139,154,170],[71,138,163],[53,119,160],[57,88,151]]
sixth_color_name=['white','black','6-1','6-2','6-3','6-4','6-5','6-6']

sixth_color_hsv = np.zeros((len(sixth_color), 1, 3),dtype='uint8')
for i in range(len(sixth_color)):
   sixth_color_hsv[i] = sixth_color[i]

sixth_color_hsv = cv2.cvtColor(sixth_color_hsv, cv2.COLOR_BGR2HSV)
sixth=blurred[round(8.1*w):round(8.9*w), round(0.2*w):round(0.8*w)]
cv2.imshow('sixth',sixth)
sixth = cv2.cvtColor(sixth, cv2.COLOR_BGR2HSV)


sixth_color_text= label(sixth,contours,sixth_color_hsv,sixth_color_name)



##############seventh######################

seventh_color=[[255,255,255],[0,0,0],[39,66,131],[140,161,199],[128,156,181],[74,128,99],[145,106,74]]
seventh_color_name=['white','black','7-1','7-2','7-3','7-4','7-5']

seventh_color_hsv = np.zeros((len(seventh_color), 1, 3),dtype='uint8')
for i in range(len(seventh_color)):
   seventh_color_hsv[i] = seventh_color[i]

seventh_color_hsv = cv2.cvtColor(seventh_color_hsv, cv2.COLOR_BGR2HSV)
seventh=blurred[round(9.6*w):round(10.4*w), round(0.2*w):round(0.8*w)]

cv2.imshow('seventh',seventh)
seventh = cv2.cvtColor(seventh, cv2.COLOR_BGR2HSV)


seventh_color_text= label(seventh,contours,seventh_color_hsv,seventh_color_name)


Result_color=np.array([first_color_text,second_color_text,third_color_text,fourth_color_text,fifth_color_text,sixth_color_text,seventh_color_text])
Result=[Health_detect(first_color_text),Health_detect(seventh_color_text),Health_detect(third_color_text)
        ,Health_detect(fourth_color_text),Health_detect(fifth_color_text),Health_detect(sixth_color_text)
        ,Health_detect(seventh_color_text)]

print(Result)




cv2.waitKey(0)


