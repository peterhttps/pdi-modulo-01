import numpy as np
from PIL import Image
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/Woman_eye.png')).convert('RGB')

a = np.array(im)

#print(a)


