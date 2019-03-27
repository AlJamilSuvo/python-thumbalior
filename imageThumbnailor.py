import cv2
import sys
import datetime as dt
start = dt.datetime.now()
fileName= sys.argv[1]
fileNameWithoutExtension = fileName.split(".")[0]
img  = cv2.imread(fileName)
r,c,__ = img.shape
result = cv2.resize(img,(200,int(200*r/c)),interpolation = cv2.INTER_LINEAR)
status = cv2.imwrite(fileNameWithoutExtension+"_thumb.jpeg",result)
print(status)