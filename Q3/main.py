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
    m = 3//2
    n = 3//2
    i = 0
    j = 0
    k = -m
    l = -n
    dfi = dfj = soma = 0

    resultado = np.zeros(img.shape, dtype='uint16') 

    vertical = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

    horizontal = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):

            count_x = 0
            for k in range(k, m+1, 1):
                count_y = 0
                for l in range(l, n+1, 1):
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        dfi += 0
                        dfj += 0
                    else:
                       #print(count_x, count_y)
                       dfi = np.add(dfi, np.multiply(vertical[count_x, count_y], img[k+i, l+j]))
                       dfj = np.add(dfj, np.multiply(horizontal[count_x, count_y], img[k+i, l+j]))
                    count_y += 1
                l = -n
                count_x += 1
            k = -m
            soma = np.add(abs(dfi), abs(dfj))
            resultado[i, j] = soma
            #print(soma)
            dfi = np.multiply(dfi, 0)
            dfj = np.multiply(dfj, 0)
            soma = 0
        j = 0

    img_resultante_sobel = Image.fromarray(resultado.astype(np.uint8))

    img_resultante_sobel.save("sosobel.png")
    
    resultado_final = histograma(resultado, img.shape)

    return resultado_final

def histograma(sob, img_shape):
    h, w, c = img_shape
    i = j = 0
    resultado = np.zeros(img_shape, dtype='uint8') 

    #print(np.amax(sob))
    #print(np.amin(sob))

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            tr = np.round_(((sob[i, j] - np.amin(sob))/(np.amax(sob) - np.amin(sob)))*((np.amax(sob) - 1) - 1)) 
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




