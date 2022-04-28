import numpy as np
from PIL import Image
import os.path
from helper import *

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/Woman.png')).convert('RGB')

a = np.array(im)

imageYIQ = transformRGB2YIQ(a)
imageRGB = Image.fromarray(transformYIQ2RGB(imageYIQ).astype(np.uint8))
imageYIQ = Image.fromarray(imageYIQ.astype(np.uint8))

imageYIQ.save("Woman_yiq.png")
imageRGB.save("Woman_yiq_back_to_rgb.png")
