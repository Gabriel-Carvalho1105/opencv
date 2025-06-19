#Olá, rede in!

import cv2 as cv # Importa biblioteca para o seu código

image = cv.imread('gato.jpg') # Armazena a imagem na variável com cores RGB
image2 = cv.imread('gato.jpg', cv.IMREAD_GRAYSCALE) # Armazena a imagem na variável com cores cinzas(GrayScale)
image_blur = cv.blur(image, (5, 5)) #Armazena a imagen Com desfoque simples 
image_gaussian = cv.GaussianBlur(image, (5, 5), 0) #Armazena a imagen Com desfoque simples porém natural
image_laplacian = cv.Laplacian(image, cv.CV_64F)#Armazena a imagem com bordas com muita de intensidade
image_laplacian_blur = cv.Laplacian(image_blur, cv.CV_64F)#Armazena a imagem com bordas com muita de intensidade
image_bordas = cv.Canny(image2, 100, 200) #armazena a imagem com bordas mais suaves


cv.imshow('ColorCat', image) #Printa na tela a imagem armazenada na variável 
cv.imshow('GrayCat', image2) #Printa na tela a imagem armazenada na variável 
cv.imshow('CatBlur', image_blur) #Printa a imagem com leve um embaçamento
cv.imshow('CatGaussian', image_gaussian) #Printa a imagen com embaçamento natural
cv.imshow('CatLaplacian', image_laplacian) #Printa a imagem com bordas intensas
cv.imshow('CatLaplacian_blur', image_laplacian_blur)
cv.imshow('CatEdges', image_bordas) #Printa na tela a imagem armazenada na variável  
cv.waitKey(0) #Mantem a janela aberta ate que o código seja fechado


