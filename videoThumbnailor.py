import cv2
import sys
import datetime as dt
start = dt.datetime.now()
fileName= sys.argv[1]
fileNameWithoutExtension = fileName.split(".")[0]
cap  = cv2.VideoCapture(fileName)
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
cap.set(cv2.CAP_PROP_POS_FRAMES,totalFrames/2)
__,img = cap.read()
# cv2.imwrite("captured.jpeg",img)
# cv2.imshow("sss",img)
cv2.waitKey()
r,c,__ = img.shape
result = cv2.resize(img,(200,int(200*r/c)),interpolation = cv2.INTER_LINEAR)
status = cv2.imwrite(fileNameWithoutExtension+"_thumb.jpeg",result)
print(status)