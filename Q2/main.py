import numpy as np
from PIL import Image
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, '../imagens/Woman.png'))
rgb_im = im.convert('RGB')

width, height = im.size

output_im = Image.new('RGB', (width,height))

for w in range(width):
    for h in range(height):
        r,g,b = rgb_im.getpixel((w,h))
        output_r = 255 - r
        output_g = 255 - g
        output_b = 255 - b
        alpha = 1
        output_im.putpixel((w, h), (output_r, output_g, output_b, alpha))

output_im.save("./Q2/rgb_negative.png")
