import numpy as np
from PIL import Image
import os.path
from helper import *

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/Woman.png')).convert('RGB')

a = np.array(im)

def mediana(img):
    h, w, c = img.shape 
    m = 3//2
    n = 5//2
    i = 0
    j = 0
    k = -m
    l = -n

    img_medianaY = np.zeros(img.shape, dtype='uint8') 

    for i in range(i, h-1, 1):
        for j in range(j, w-1, 1):
            medianaY = []

            for k in range(k, m+1, 1):
                for l in range(l, n+1, 1):
                    if (k+i < 0 or k+i > h-1) or (l+j < 0 or l+j > w-1):
                        medianaY.append(0)
                    else:
                        medianaY.append(img[i+k, j+l, 0])
                l = -n
            k = -m

            medianaY = np.sort(medianaY)

            y = np.median(medianaY)
            I = img[i, j, 1]
            q = img[i, j, 2]

            #print(i, j)
            img_medianaY[i, j] = y
        j = 0
    return img_medianaY

img_yiq = transformRGB2YIQ(a)

img_resultante = mediana(img_yiq)

img_resultante_yiq = Image.fromarray(img_resultante.astype(np.uint8))
img_resultante_rgb = Image.fromarray(transformYIQ2RGB(img_resultante).astype(np.uint8))

img_resultante_yiq.save("./Q4/medianaY_yiq.png")
img_resultante_rgb.save("./Q4/medianaY_rgb.png")