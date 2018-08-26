import numpy as np
import os
import glob

index_i=0
index_j=0

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
        if(str(a)[2]=='0' and len(str(a))==3):
            index_j = int(d)
        else:
            index_j = int(d) - index_i*220
    elif(len(img4)==5):
        d = img4[0] + img4[2] + img4[4]
        a = float(str(d))/219.0
        index_i = int(str(a)[0])
        if(str(a)[2]=='0' and len(str(a))==3):
            index_j = int(d)
        else:
            index_j = int(d) - index_i*220
    else:
        a = float(str(img4))/219.0
        index_i = int(str(a)[0])
        if(str(a)[2]=='0' and len(str(a))==3):
            index_j = int(img3)
        else:
            index_j = int(img3) - index_i*220


    if(index_j==219):
        index_j=0
        index_i+=1
    else:
        index_j+=1
    return index_i, index_j

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
    index_i, index_j = index()
    print index_i, index_j
    file.write(porcentaje + " " + str(index_i) + " " + str(index_j - 1) + "\n")
    os.system("rm output.txt")
    os.system("rm output.tx")
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
    index_i, index_j = index()
    file.write(porcentaje + " " + str(index_i) + " " + str(index_j-1) + "\n")
    file.close()
    os.system("rm output.txt")
    os.system("rm output.tx")
