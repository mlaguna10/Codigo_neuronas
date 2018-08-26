import numpy as np
import os
import glob

index_i=0
index_j=0

def iteracion():
    if(index_i==109 and index_j==109):
        s=0
    else:
        os.system("make")

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
    a = float(str(img3))/219.0
    index_i = int(str(a)[0])
    if(str(a)[2]=='0' and len(str(a))==3):
        index_j = int(img3)
    else:
        index_j = int(img3) - index_i*219 - 1

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

fp.close()

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
file.write(porcentaje)
index()
file.write(porcentaje + " " + str(index_i) + " " + str(index_j))
file.close()
os.system("rm output.txt")
os.system("rm output.tx")
iteracion()
