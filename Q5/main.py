import numpy as np
import os
import cv2 as cv
from matplotlib import pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
img_woman = cv.imread(os.path.join(script_dir, '../imagens/Woman.png'),0)
template = cv.imread(os.path.join(script_dir, '../imagens/Woman_eye.png'),0)

w, h = template.shape[::-1]

img_copy = img_woman.copy()
method = cv.TM_CCORR_NORMED

result = cv.matchTemplate(img_copy,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img_copy,top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(result,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_copy,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()

cv.rectangle(img_copy,top_left, bottom_right, 255, -1)

method = cv.TM_CCORR_NORMED

result = cv.matchTemplate(img_copy,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img_copy,top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(result,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_copy,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()  
