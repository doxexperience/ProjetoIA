#importar o opencv
import cv2

#capturar video   cap=variavel capturar
cap = cv2.VideoCapture('pessoas.mp4')

#criar loop
while(True):

    #recuperar os frames  ret=variavel retorno
    ret, frame = cap.read()

    #se tiver ret
    if ret:

        #mostrar o frame
        cv2.imshow('frame', frame)

    #recupera o botao apertar
    Key = cv2.waitKey(30)

    if Key == ord('q'):
        break

#libera o cache de cap
cap.release()

#destruir as janelas abertas
cv2.destroyAllWindows