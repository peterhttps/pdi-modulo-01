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

            for k in range(k, m+1, 1):
                for l in range(l, n+1, 1):
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        #soma 0
                        pass
                    else:
                        mediaR += img[i+k, j+l, 0]*mascara_media[k+m, l+n]
                        mediaG += img[i+k, j+l, 1]*mascara_media[k+m, l+n]
                        mediaB += img[i+k, j+l, 2]*mascara_media[k+m, l+n]
                l = -n
            k = -m

            r = mediaR
            g = mediaG
            b = mediaB

            img_media[i, j] = [r + offset, g + offset, b + offset]
        j = pivo[1]

    return img_media

def sobel(img):
    h, w, c = img.shape
    dfiR = dfiG = dfiB = dfjR = dfjG = dfjB = 0
    offset = 0
    pivo = [0, 0]
    i = pivo[0]
    j = pivo[1]
    m = 3//2
    k = l = -m
    x = y = 0

    vertical = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

    horizontal = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

    resultado_final_horizontal = np.zeros(img.shape, dtype='uint16')
    resultado_final_vertical = np.zeros(img.shape, dtype='uint16')
    resultado_final = np.zeros(img.shape, dtype='uint16')

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
           
            for k in range(k, m+1, 1):
                for l in range(l, m+1, 1):
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        #soma 0
                        pass
                    else:
                        dfiR = np.add(dfiR, np.multiply(img[i+k, j+l, 0],vertical[k+m, l+m]))
                        dfiG = np.add(dfiG, np.multiply(img[i+k, j+l, 1],vertical[k+m, l+m]))
                        dfiB = np.add(dfiB, np.multiply(img[i+k, j+l, 2],vertical[k+m, l+m]))
                        dfjR = np.add(dfjR, np.multiply(img[i+k, j+l, 0],horizontal[k+m, l+m]))
                        dfjG = np.add(dfjG, np.multiply(img[i+k, j+l, 1],horizontal[k+m, l+m]))
                        dfjB = np.add(dfjB, np.multiply(img[i+k, j+l, 2],horizontal[k+m, l+m]))
                l = -m
            k = -m
            resultado_final_horizontal[i, j] = [np.absolute(dfiR), np.absolute(dfiG), np.absolute(dfiB)]
            resultado_final_vertical[i, j] = [np.absolute(dfjR), np.absolute(dfjG), np.absolute(dfjB)]
            somaR = np.absolute(dfiR) + np.absolute(dfjR)
            somaG = np.absolute(dfiG) + np.absolute(dfjG)
            somaB = np.absolute(dfiB) + np.absolute(dfjB)
            resultado_final[i, j] = [somaR, somaG, somaB]
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
    
    resultado_histograma_vertical = histograma(resultado_final_vertical, img.shape, offset)
    resultado_histograma_horizontal = histograma(resultado_final_horizontal, img.shape, offset)
    resultado_histograma = histograma(resultado_final, img.shape, offset)

    img_resultante_vertical = Image.fromarray(resultado_final_vertical.astype(np.uint8))
    img_resultante_horizontal = Image.fromarray(resultado_final_horizontal.astype(np.uint8))

    img_resultante_vertical.save("sobel_vertical.png")
    img_resultante_horizontal.save("sobel_horizontal.png")

    return resultado_histograma

def histograma(sob, img_shape, offset):
    sobR, sobG, sobB = np.split(sob, 3, axis=2)
    h, w, c = img_shape
    i = j = 0
    maiorR = np.amax(sobR)
    maiorG = np.amax(sobG)
    maiorB = np.amax(sobB)
    menorR = np.amin(sobR)
    menorG = np.amin(sobG)
    menorB = np.amin(sobB)

    resultado = np.zeros([h, w, c], dtype='uint8') 

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            trR = np.round_(np.multiply(np.divide(sob[i, j, 0] - menorR, maiorR - menorR), 254))
            trG = np.round_(np.multiply(np.divide(sob[i, j, 1] - menorG, maiorG - menorG), 254))
            trB = np.round_(np.multiply(np.divide(sob[i, j, 2] - menorB, maiorB - menorB), 254))
            resultado[i, j] = [trR + offset, trG + offset, trB + offset]
        j = 0

    return resultado

img_resultante_sobel = sobel(a)

img_resultante_rgb2 = Image.fromarray(img_resultante_sobel.astype(np.uint8))

img_resultante_rgb2.save("sobel.png")




