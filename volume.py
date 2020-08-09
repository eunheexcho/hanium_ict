import cv2
import numpy as np
from scipy.spatial import distance as dist

img = cv2.imread('vol.png',0)





img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cimg_original = cimg.copy()

# Circle Detection
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=26,minRadius=0,maxRadius=0)

print(circles)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)



img_line=cv2.imread('vol.png')
img_line_original=img_line.copy()
height, width, channel = img_line.shape
print([height,width])

gray = cv2.cvtColor(img_line, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,0,1,apertureSize=3)
cv2.imshow('edge',edges)

# Line Detection
lines = cv2.HoughLinesP(edges, 0.2, np.pi / 180, 100)

c=[]

start_point=lines[:,0][:,0:2]
end_point=lines[:,0][:,2:]
print(len(lines))
for k in range(0,len(lines)):

# Only detect line that we want
    if dist.euclidean(start_point[k],end_point[k])>100:
        if dist.euclidean(start_point[k],end_point[k])<200:
            c.append(k)

print(c)



cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

