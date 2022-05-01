import numpy as np
from PIL import Image
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/woman.png')).convert('RGB')

a = np.array(im)

def media(img):
    h, w, c = img.shape 
    offset = 25
    pivo = [0, 0]
    row = 5
    col = 3
    m = col//2
    n = row//2
    i = pivo[0]
    j = pivo[1]
    k = -m
    l = -n

    img_media = np.zeros(img.shape, dtype='uint8') 

    mascara_media = np.full([row, col, 1], 1/(row*col), dtype='float')

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            mediaR = 0
            mediaG = 0
            mediaB = 0

            for k in range(k, m, 1):
                for l in range(l, n, 1):
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        pass
                    else:
                        #print(k, j)
                        mediaR += img[i+k, j+l, 0]*mascara_media[k, l]
                        mediaG += img[i+k, j+l, 1]*mascara_media[k, l]
                        mediaB += img[i+k, j+l, 2]*mascara_media[k, l]
                l = -n
            k = -m

            r = mediaR
            g = mediaG
            b = mediaB

            #print(i, j)
            img_media[i, j] = [r + offset, g + offset, b + offset]
        j = pivo[1]

    return img_media

def sobel(img):
    h, w, c = img.shape
    dfiR = dfiG = dfiB = dfjR = dfjG = dfjB = 0
    offset = 25
    pivo = [0, 0]
    i = pivo[0]
    j = pivo[1]
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
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        pass
                    else:
                        dfiR = np.add(dfiR, np.multiply(img[i+k, j+l, 0],vertical[k, l]))
                        dfiG = np.add(dfiG, np.multiply(img[i+k, j+l, 1],vertical[k, l]))
                        dfiB = np.add(dfiB, np.multiply(img[i+k, j+l, 2],vertical[k, l]))
                        dfjR = np.add(dfjR, np.multiply(img[i+k, j+l, 0],horizontal[k, l]))
                        dfjG = np.add(dfjG, np.multiply(img[i+k, j+l, 1],horizontal[k, l]))
                        dfjB = np.add(dfjB, np.multiply(img[i+k, j+l, 2],horizontal[k, l]))
                l = 0 
            k = 0
            somaR = np.absolute(dfiR) + np.absolute(dfjR)
            somaG = np.absolute(dfiG) + np.absolute(dfjG)
            somaB = np.absolute(dfiB) + np.absolute(dfjB)
            resultado_final[i, j] = [somaR + offset, somaG + offset, somaB + offset]
            dfiR = 0
            dfiG = 0
            dfiB = 0
            dfjR = 0
            dfjG = 0
            dfjB = 0
            somaR = 0
            somaG = 0
            somaB = 0
        j = pivo[1] 

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

img_resultante_media = media(a)
img_resultante_sobel = sobel(a)

img_resultante_rgb = Image.fromarray(img_resultante_media.astype(np.uint8))
img_resultante_rgb2 = Image.fromarray(img_resultante_sobel.astype(np.uint8))

img_resultante_rgb.save("media.png")
img_resultante_rgb2.save("sobel.png")




