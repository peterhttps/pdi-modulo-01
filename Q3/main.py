import numpy as np
from PIL import Image
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/maquina.png')).convert('RGB')

a = np.array(im)

def mediana(img):
    h, w, c = img.shape 
    m = 3//2
    n = 9//2
    i = 0
    j = 0
    k = -m
    l = -n

    img_mediana = np.zeros(img.shape, dtype='uint8') 

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            medianaR = []
            medianaG = []
            medianaB = []

            for k in range(k, m+1, 1):
                for l in range(l, n+1, 1):
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        medianaR.append(0)
                        medianaG.append(0)
                        medianaB.append(0)
                    else:
                        medianaR.append(img[i+k, j+l, 0])
                        medianaG.append(img[i+k, j+l, 1])
                        medianaB.append(img[i+k, j+l, 2])
                l = -n
            k = -m

            medianaR = np.sort(medianaR)
            medianaG = np.sort(medianaG)
            medianaB = np.sort(medianaB)

            r = np.median(medianaR)
            g = np.median(medianaG)
            b = np.median(medianaB)

            #print(i, j)
            img_mediana[i, j] = [r, g, b]
        j = 0
    return img_mediana

def sobel(img):
    h, w, c = img.shape
    dfi = dfj = 0
    i = j = 0
    k = l = 0
    x = y = 0
    m = 3

    vertical = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

    horizontal = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

    resultado_final = np.zeros(img.shape, dtype='uint16')

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
           
            for k in range(k, m, 1):
                for l in range(l, m, 1):
                    if (k+i+1 < 0 or k+i+1 > h-1) or (l+j+1 < 0 or l+j+1 > w-1):
                        pass
                    else:
                        dfi = np.add(dfi, np.multiply(img[i+k+1, j+l+1, 0],vertical[k, l]))
                        dfj = np.add(dfj, np.multiply(img[i+k+1, j+l+1, 0],horizontal[k, l]))
                        #print(img[i+k+1, j+l+1], vertical[k, l], dfi)
                l = 0 
            k = 0
            soma = np.absolute(dfi) + np.absolute(dfj)
            #print(soma)
            resultado_final[i, j] = soma
            dfi = 0
            dfj = 0
            soma = 0
        j = 0    

    img_resultante_sobel = Image.fromarray(resultado_final.astype(np.uint8))

    img_resultante_sobel.save("sosobel.png")
    
    resultado_histograma = histograma(resultado_final, img.shape)

    return resultado_histograma

def histograma(sob, img_shape):
    h, w, c = img_shape
    i = j = 0
    maior = np.amax(sob)
    menor = np.amin(sob)
    resultado = np.zeros(img_shape, dtype='uint8') 

    #print(maior, menor)

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            tr = np.round_(np.multiply(np.divide(np.subtract(sob[i, j, 0], menor), maior - menor), 254))
            resultado[i, j] = tr
        j = 0
    #print(resultado)

    return resultado

img_resultante_mediana = mediana(a)
img_resultante_sobel = sobel(a)

img_resultante_rgb = Image.fromarray(img_resultante_mediana.astype(np.uint8))
img_resultante_rgb2 = Image.fromarray(img_resultante_sobel.astype(np.uint8))

img_resultante_rgb.save("medianaRGB.png")
img_resultante_rgb2.save("sobel.png")




