import  cv2 as cv

#depositivo a captura
video=cv.VideoCapture(0,cv.CAP_DSHOW)
classificador=cv.CascadeClassifier("cascadecadeirante.xml")


while True:

    conectado,frame = video.read()
    #print(conectado) #mostra se tá conectado
    #print(frame) #mostra o frame semelhante os rectangulo x y l a

    frameCinza=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faceDetect= classificador.detectMultiScale(frameCinza,scaleFactor=1.1,minSize=(200,200),minNeighbors=20)

    for (x,y,l,a) in faceDetect:
        cv.rectangle(frame, (x,y),(x+l,y+a),(255,0,0),2)

    cv.imshow("cam",frame)

    #q equivale a 1 e dá um break
    if cv.waitKey(1) == ord('q'):
        break


#liberar a capitura
video.release()
#liberar memoria
cv.destroyAllWindows()