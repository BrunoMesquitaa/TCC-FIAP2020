import cv2

classificador=cv2.CascadeClassifier("cascadecadeirante.xml")
img=cv2.imread("Acessibilidade.jpg")
imgC=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
classCaneca=classificador.detectMultiScale(imgC,scaleFactor=1.1,minSize=(100,100),minNeighbors=10)

for (x,y,l,a) in classCaneca:
    cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),5)

cv2.imshow("",img)
cv2.waitKey()
