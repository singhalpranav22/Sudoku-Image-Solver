import cv2
import os
import numpy as np
from utility import *
path = "Resources/1.jpg"
imgH = 640
imgW = 640

img = cv2.imread(path)
img = cv2.resize(img,(imgW,imgH))
imgBlank = np.zeros((imgH,imgW,3),np.uint8)
imgTreshold = preProcessing(img)

imgContours = img.copy()
imgBigContours = img.copy()
contours,hierarchy = cv2.findContours(imgTreshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgContours,contours,-1,(0,255,0),3)

biggest,maxArea = biggestContour(contours)
print(biggest)






imgArray = ([img,imgTreshold,imgContours],[imgBlank,imgBlank,imgBlank])
stackImg = stackImages(imgArray,1)
cv2.imshow("Output",stackImg)
cv2.waitKey(0)
