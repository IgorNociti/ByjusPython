import cv2

img = cv2.imread("cachorro_azul - Copia.jpg")

cv2.imshow("Imagem de Exibicao",img)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Escala de Cinzas", gray_img)
cv2.waitKey(0)