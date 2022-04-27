import numpy as np
from PIL import Image, ImageDraw
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
im_woman = Image.open(os.path.join(script_dir, '../imagens/Woman.png')).convert('RGB')
im_woman_eye   = Image.open(os.path.join(script_dir, '../imagens/Woman_eye.png')).convert('RGB')

arr_woman = np.asarray(im_woman)
arr_woman_eye = np.asarray(im_woman_eye)

y_woman, x_woman = arr_woman.shape[:2]
y_woman_eye, x_woman_eye = arr_woman_eye.shape[:2]

xstop = x_woman - x_woman_eye + 1
ystop = y_woman - y_woman_eye + 1

matches = []
for x_min in range(0, xstop):
    for y_min in range(0, ystop):
        x_max = x_min + x_woman_eye
        y_max = y_min + y_woman_eye

        arr_s = arr_woman[y_min:y_max, x_min:x_max]   
        arr_t = (arr_s == arr_woman_eye)                
        if arr_t.all():                         
            matches.append((x_min,y_min))


img_drawing = ImageDraw.Draw(im_woman)
img_drawing.rectangle((matches[0], (np.asarray(im_woman_eye).shape[1] + 247, np.asarray(im_woman_eye).shape[0] + 184)), outline="red", width=2)
im_woman.show()

