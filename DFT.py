#(Extra): http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php
#Creditos: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import sys
import glob

n=0

def escribir(index_i, index_j):
    filepath = 'output.txt'
    archivo = 'porcentajes.txt'
    porcentaje = ""
    linea = ""

    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if(cnt == 4):
                linea = "Line {}: {}".format(cnt, line.strip())
            line = fp.readline()
            cnt += 1

    if(str(glob.glob('frec*')) == '[]'):
        file = open(archivo,"w")
        z = []
        value = False
        for letter in linea:
            if(value):
                z.append(letter)
            else:
                if(letter==str(0)):
                    z.append(letter)
                    value = True
        s = ''.join(map(str,z))
        porcentaje = s.replace(")","")
        file.write(porcentaje + " " + str(index_i) + " " + str(index_j) + "\n")
        os.system("rm output.txt")
    else:
        file = open(archivo,"a")
        z = []
        value = False
        for letter in linea:
            if(value):
                z.append(letter)
            else:
                if(letter==str(0)):
                    z.append(letter)
                    value = True
        s = ''.join(map(str,z))
        porcentaje = s.replace(")","")
        file.write(porcentaje + " " + str(index_i) + " " + str(index_j) + "\n")
        file.close()
        os.system("rm output.txt")

def inicio(index_i, index_j):
    imagen = str(glob.glob('frec*'))
    if(imagen == '[]'):
        plt.savefig('frec_' + str(index_i*219 + index_j) + ".png",bbox_inches='tight', pad_inches=-0.1)
        f = open("output.txt", "w")
        h = os.popen("python scripts/label_image.py --image frec_" + str(index_i*219 + index_j) + ".png").read()
        f.write(h)
        f.close()
        escribir(index_i, index_j)
    else:
        #factor de compensacion
        if(index_j==0):
            n=1
        else:
            if(index_i!=0):
                if(index_j%219==0):
                    n=0
                else:
                    n=1
            else:
                n=0
        os.system("rm frec_*")
        plt.savefig('frec_' + str(index_i*219 + index_j + n) + ".png",bbox_inches='tight', pad_inches=-0.1)
        f = open("output.txt", 'w')
        h = os.popen("python scripts/label_image.py --image frec_" + str(index_i*219 + index_j + n) + ".png").read()
        f.write(h)
        f.close()
        escribir(index_i, index_j)
    return index_i, index_j

def index():
    z=[]
    imagen = str(glob.glob('frec*'))
    img1 = imagen.replace("[","")
    img2 = img1.replace("]","")
    img3 = img2.replace("'","")
    i = img3.index('_')
    while(img3[i+1]!='.'):
        z.append(img3[i+1])
        i+=1
    img1 = str(z).replace("[","")
    img2 = img1.replace("]","")
    img3 = img2.replace("'","")
    img4 = img3.replace(",","")
    if(len(img4)==3):
        d = img4[0] + img4[2]
        a = float(str(d))/219.0
        index_i = int(str(a)[0])
        index_j = int(str(d))+1
    elif(len(img4)==5):
        d = img4[0] + img4[2] + img4[4]
        a = float(str(d))/219.0
        index_i = int(str(a)[0])
        if(str(a)[2]=='0' and len(str(a))==3):
            index_j=0
        elif(float(str(d))==(219.0*(index_i+1)-1)):
            index_j = int(str(d)) + 1 - 219*index_i
        else:
            if(index_i!=0):
                if(index_i==1):
                    index_j=(int(str(d))%(220*index_i - (index_i)))
                else:
                    index_j=(int(str(d))%(220*index_i - (index_i-1)))+1
            else:
                index_j = int(str(d))+1
    elif(len(img4)==7):
        d = img4[0] + img4[2] + img4[4] + img4[6]
        a = float(str(d))/219.0
        if(str(a)[1]!="."):
            index_i = int(str(a)[0] + str(a)[1])
        else:
            index_i = int(str(a)[0])
        if(float(str(d))==(219.0*(index_i+1)-1)):
            index_j = int(str(d)) + 1 - 219*index_i
        elif(len(str(index_i))!=1):
            if(str(a)[3]=='0' and len(str(a))==4):
                index_j = 0
            else:
                index_j=(int(str(d))%(220*index_i - (index_i-1)))+1
        else:
            if(str(a)[2]=='0' and len(str(a))==3):
                index_j = 0
            else:
                index_j=(int(str(d))%(220*index_i - (index_i-1)))+1
    elif(len(img4)==9):
        d = img4[0] + img4[2] + img4[4] + img4[6] + img4[8]
        a = float(str(d))/219.0
        if(str(a)[2]!="."):
            index_i = int(str(a)[0] + str(a)[1] + str(a)[2])
        else:
            index_i = int(str(a)[0] + str(a)[1])
        if(float(str(d))==(219.0*(index_i+1)-1)):
            index_j = int(str(d)) + 1 - 219*index_i
        elif(len(str(index_i))!=2):
            if(str(a)[4]=='0' and len(str(a))==5):
                index_j = 0
            else:
                index_j=(int(str(d))%(220*index_i - (index_i-1)))+1
        else:
            if(str(a)[3]=='0' and len(str(a))==4):
                index_j = 0
            else:
                index_j=(int(str(d))%(220*index_i - (index_i-1)))+1
    else:
        d = img4[0]
        a = float(str(d))/219.0
        index_i = int(str(a)[0])
        index_j= int(str(d))+1

    return index_i, index_j

def cut_off_frec(frec,i,j):
    if(i==0 and j==0):
        frec[0][0] = 0
    else:
        frec[i][j]=0
        if(j==0):
            i=i-1
            j=j+219
            frec[219-i][219-j]=0
        else:
            frec[219-i][219-j+1]=0
    return frec

if(str(glob.glob('frec*')) == '[]'):
    index_i=0
    index_j=0
    img = cv2.imread('gray_rose.jpg',0)
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft = cut_off_frec(dft,index_i,index_j)
    img_back = cv2.idft(dft)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
    fig = plt.figure()
    fig.set_size_inches(3.56,3.56)
    plt.imshow(img_back,cmap='gray')
    plt.xticks([]), plt.yticks([])
    index_i, index_j = inicio(index_i, index_j)
else:
    index_i, index_j = index()
    img = cv2.imread('gray_rose.jpg',0)
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    print index_i, index_j
    dft = cut_off_frec(dft,index_i,index_j)
    img_back = cv2.idft(dft)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
    fig = plt.figure()
    fig.set_size_inches(3.56,3.56)
    plt.imshow(img_back,cmap='gray')
    plt.xticks([]), plt.yticks([])
    index_i, index_j = inicio(index_i, index_j)
