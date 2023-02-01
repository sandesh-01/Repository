import cv2
face1=  cv2.cascadeclassifier('haarcascade_frontalface_default.xml')
img=cv2.imread("1.jpeg")
g1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
F1=face_cascade.DetectMultiscale(gray,1,5)
for (x,y,w,z) in f1:
  cv2.rectangle(img ,(x,y),(x+w,y+z),(255,255,255),2)
cv2.imshow("1",1)
cv2.wait(20)
