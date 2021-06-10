import numpy as np
import cv2
import os
from PIL import Image

#7712
eyes = np.zeros((128,128))
n_actual = 0
dim = (50,50)


for i in range(0,30000):
    file = "img_%s.jpg" %i
    if os.path.exists(file):
        eyes= (np.array(Image.open(file)))
        n_actual+=1
        img_name = "filtered/img_%s.jpg" %n_actual
        eyes = cv2.resize(eyes, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(img_name,eyes)
    else:
        print(file, "NO Existe")