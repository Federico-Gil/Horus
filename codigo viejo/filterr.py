from size_normalizer import normalize_size
import numpy as np
from PIL import Image
import os


def get_size(filename):
    if os.path.exists(filename):
        img = Image.open(filename)
        print(img.size)
        return img.size[0]
    else:
        return

def filter_and_normalizer(img_name):
    if get_size(img_name) < 32:
        os.remove(img_name)
    else:
        normalize_size(img_name,32)
"""
for i in range (0,200):
    name = 'img_%s.jpg' %i
    print(get_size(name))
"""
print(get_size('img_test_2.jpg'))