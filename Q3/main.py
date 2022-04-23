import numpy as np
from PIL import Image

im = Image.open("../imagens/Woman.png").convert('RGB')

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

img_resultante = mediana(a)

img_resultante_rgb = Image.fromarray(img_resultante.astype(np.uint8))

img_resultante_rgb.save("../imagens/medianaRGB.png")




