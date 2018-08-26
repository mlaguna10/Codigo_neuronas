#(Extra): http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php
#Creditos: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import sys
import glob

N = 220
index_i=0
index_j=0

def inicio():
    imagen = str(glob.glob('frec*'))
    if(imagen == '[]'):
        plt.savefig('frec_' + str(index_i*219 + index_j) + ".png",bbox_inches='tight', pad_inches=-0.1)
        f = open("output.txt", "w")
        h = os.popen("python scripts/label_image.py --image frec_" + str(index_i*219 + index_j) + ".png").read()
        f.write(h)
        f.close()
    else:
        index()
        os.system("rm frec_*")
        plt.savefig('frec_' + str(index_i*219 + index_j) + ".png",bbox_inches='tight', pad_inches=-0.1)
        f = open("output.txt", 'w')
        h = os.popen("python scripts/label_image.py --image frec_" + str(index_i*219 + index_j) + ".png").read()
        f.write(h)
        f.close()

def index():
    z=[]
    imagen = str(glob.glob('frec*'))
    img1 = imagen.replace("[","")
    img2 = img1.replace("]","")
    img3 = img2.replace("'","")
    i = img3.index('_')
    while(img3[i]!="."):
        z.append(img3[i])
    a = float(z)/219.0
    index_i = int(str(a)[0])
    if(a[2]==0 and len(str(a)==3)):
        index_j = int(z)
    else:
        index_j = int(z) - index_i*219 - 1

def cut_off_frec(frec,i,j):
    if(i==0 and j==0):
        frec[0][0] = 0
    else:
        frec[i][j]=0
        if(i==0 and j==1):
            frec[219-i][220-j]=0
        else:
            frec[219-i][219-j]=0
    return frec

img = cv2.imread('gray_rose.jpg',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft = cut_off_frec(dft,index_i,index_j)
img_back = cv2.idft(dft)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
fig = plt.figure()
fig.set_size_inches(3.56,3.56)
plt.imshow(img_back,cmap='gray')
plt.xticks([]), plt.yticks([])
inicio()
