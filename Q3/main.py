import numpy as np
from PIL import Image

im = Image.open("../imagens/Woman_eye.png").convert('RGB')

a = np.array(im)

#print(a)


