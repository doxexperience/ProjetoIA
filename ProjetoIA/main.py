#importar openCV
import cv2

#p/ abrir a imagem
img = cv2.imread('dox.png')

#mostrar a imagem
cv2.imshow('dox.png',img)

#salvar nova imagem
cv2.imwrite('doxexpereince.png', img)

#usar o roi ,primeiro altura dps largura
roi = img[75:300, 100:300]

#mostrar o roi
cv2.imshow('roi', roi)

#imagem redimensionada 
imgresize = cv2.resize(img, (600,600))

#mostrar o imgresize
cv2.imshow('imgresize', imgresize)

#pausa (esperar apertar uma tecla)
cv2.waitKey(0)
