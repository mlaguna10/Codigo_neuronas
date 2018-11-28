import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import sys
import cmath as mt
import glob
from PIL import Image

dim_x = 0
dim_y = 0

def rutas(files):
    for i in range(len(files)):
        pdf_name = files[i].split("]")[0]
        files[i] = pdf_name
    return files

fn = sys.argv[1]
if os.path.exists(fn):
    dir = os.path.basename(fn)

    for folder, sub_folders, files in os.walk(dir):
        archivos = rutas(files)

file = open('tamanios',"w")
for j in range(len(archivos)):
    path = os.path.abspath("tulips/" + archivos[j])
    img = Image.open(path)
    dim_x, dim_y = img.size
    if(dim_x>dim_y):
        file.write(str(dim_x) + "\n")
    else:
        file.write(str(dim_y) + "\n")
file.close()
