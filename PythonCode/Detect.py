import cv2
import time
import glob

images = []
for img in glob.glob("Imagens/*"):
    images.append(img)


classificador = cv2.CascadeClassifier("cascadecadeirante.xml")

imgVermelho = cv2.imread("01.05.jpg")
imgVerde = cv2.imread("breno-semafori-abbattuti-danni-539738.660x368.jpg")

print(images)

for imagem in images:

    img=cv2.imread(imagem)
    imgC = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    classCadeirante = classificador.detectMultiScale(imgC,scaleFactor=1.1,minSize=(125,125),minNeighbors=10)

    countCadeirante = len(classCadeirante)

    if countCadeirante > 0:
        temp = 5
    else:
        temp = 1

    for t in range(temp,-1,-1):

        img = cv2.imread(imagem)

        for (x, y, l, a) in classCadeirante:
            img = cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 0), 2)

        img=cv2.putText(img, str(t), (100, 80),cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)
        cv2.imshow("1",img)


        #if countCadeirante > 0:
        #    cv2.imshow("2", imgVermelho)
        #else:
        #    cv2.imshow("2", imgVerde)

        time.sleep(1)
        t -= 1

        if cv2.waitKey(1) & 0XFF == 27:
            break

cv2.destroyAllWindows()

