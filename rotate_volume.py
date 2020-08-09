import cv2
import numpy as np
from scipy.spatial import distance as dist
import sys
import math


img_line=cv2.imread('volume_left.png')
cv2.imshow('original',img_line)
img_line_original=img_line.copy()
height, width, channel = img_line.shape
print([height,width])

gray = cv2.cvtColor(img_line, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,0,1,apertureSize=3)
cv2.imshow('edge',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 0.7, np.pi / 180, 70)
print(lines)
c=[]
print('line1')
print(lines)
print(lines[:,0][:,0:2])
start_point=lines[:,0][:,0:2]
end_point=lines[:,0][:,2:]
print(len(lines))
# for k in range(0,len(lines)):
#
#
#     if dist.euclidean(start_point[k],end_point[k])>100:
#         if dist.euclidean(start_point[k],end_point[k])<200:
#             c.append(k)

print(c)