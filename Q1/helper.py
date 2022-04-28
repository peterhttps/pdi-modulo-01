import numpy as np

def transformRGB2YIQ(imgRGB):
    h, w, c = imgRGB.shape
    i = j = 0
    m = 3

    resultado_final = np.zeros(imgRGB.shape, dtype='uint8')

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            y = (imgRGB[i, j, 0]*0.299) + (imgRGB[i, j, 1]*0.587) + (imgRGB[i, j, 2]*0.114)
            I = (imgRGB[i, j, 0]*0.59590059) + (imgRGB[i, j, 1]*-0.27455667) + (imgRGB[i, j, 2]*-0.32134392)
            q = (imgRGB[i, j, 0]*0.21153661) + (imgRGB[i, j, 1]*-0.52273617) + (imgRGB[i, j, 2]*0.31119955)
            y = validacao(y)
            I = validacao(I)
            q = validacao(q)
            resultado_final[i, j] = [y, I, q]
        j = 0

    return resultado_final



def transformYIQ2RGB(imgYIQ):
    h, w, c = imgYIQ.shape
    i = j = 0
    m = 3

    resultado_final = np.zeros(imgYIQ.shape, dtype='uint8')

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            r = (imgYIQ[i, j, 0]*1) + (imgYIQ[i, j, 1]*0.956) + (imgYIQ[i, j, 2]*0.619)
            g = (imgYIQ[i, j, 0]*1) + (imgYIQ[i, j, 1]*-0.272) + (imgYIQ[i, j, 2]*-0.647)
            b = (imgYIQ[i, j, 0]*1) + (imgYIQ[i, j, 1]*-1.106) + (imgYIQ[i, j, 2]*1.703)
            r = validacao(r)
            g = validacao(g)
            b = validacao(b)
            resultado_final[i, j] = [r, g, b]
        j = 0

    return resultado_final

def validacao(a):
    if(a < 0):
        a = 0
    elif(a > 255):
        a = 255
         
    return a