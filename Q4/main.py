import numpy as np
from PIL import Image

im = Image.open("../imagens/Woman.png").convert('RGB')

a = np.array(im)

#print(a)

def transformRGB2YIQ(imgRGB: np.ndarray) -> np.ndarray:
    yiq_from_rgb = np.array([[0.299, 0.587, 0.114],
                             [0.59590059, -0.27455667, -0.32134392],
                             [0.21153661, -0.52273617, 0.31119955]])
    OrigShape=imgRGB.shape
    return np.dot(imgRGB.reshape(-1,3), yiq_from_rgb.transpose()).reshape(OrigShape)

    pass

def transformYIQ2RGB(imgYIQ: np.ndarray) -> np.ndarray:
    yiq_from_rgb = np.array([[0.299, 0.587, 0.114],
                             [0.59590059, -0.27455667, -0.32134392],
                             [0.21153661, -0.52273617, 0.31119955]])
    OrigShape=imgYIQ.shape
    return np.dot(imgYIQ.reshape(-1,3), np.linalg.inv(yiq_from_rgb).transpose()).reshape(OrigShape)

    pass

def mediana(img):
    h, w, c = img.shape 
    m = 3//2
    n = 5//2
    i = 0
    j = 0
    k = -m
    l = -n

    img_medianaY = np.zeros(img.shape, dtype='uint8') 

    for i in range(i, h-1, m):
        for j in range(j, w-1, n):
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

img_resultante_yiq.save("../imagens/medianaY_yiq.png")
img_resultante_rgb.save("../imagens/medianaY_rgb.png")