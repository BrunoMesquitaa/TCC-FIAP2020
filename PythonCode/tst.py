import cv2

img = cv2.imread("Imagens/Acessibilidade.jpg") #load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
value=10
for x in range(0, len(hsv)):
    for y in range(0, len(hsv[0])):
        hsv[x, y][2] += value

img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("image_processed.jpg", img)

classificador = cv2.CascadeClassifier("cascadecadeirante.xml")
imgC = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
classCadeirante = classificador.detectMultiScale(imgC,scaleFactor=1.1,minSize=(125,125),minNeighbors=5)

for (x, y, l, a) in classCadeirante:
    img = cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 0), 2)

cv2.imshow("1", img)

cv2.waitKey()
cv2.destroyAllWindows()