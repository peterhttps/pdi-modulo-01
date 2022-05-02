import numpy as np
from PIL import Image
import os.path
from helper import *

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/Woman.png'))
rgb_im = im.convert('RGB')

im_width, im_height = im.size

output_im = Image.new('RGB', (im_width, im_height))

for w in range(im_width):
    for h in range(im_height):
        r, g, b = rgb_im.getpixel((w,h))
        output_r = 255 - r
        output_g = 255 - g
        output_b = 255 - b
        alpha = 1
        output_im.putpixel((w, h), (output_r, output_g, output_b, alpha))

output_im.save("rgb_negative.png")


a = np.array(rgb_im)

img_yiq = transformRGB2YIQ(a)


for w in range(img_yiq.shape[0]):
    for h in range(img_yiq.shape[1]):
        y, i, q = img_yiq[w,h]
        img_yiq[w,h] = [255-y, i, q]
        
imageRGB = Image.fromarray(transformYIQ2RGB(img_yiq).astype(np.uint8))

imageRGB.save("yiq_negative.png")
