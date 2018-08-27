import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


porc = 'porcentajes.txt'
porc2 = 'porcentajes2.txt'
index_i = []
index_j = []
values = []
index_i2 = []
index_j2 = []
values2 = []

def p1():
    file1 = open(porc,'r')
    line = file1.readline()
    while line:
        val, i, j = line.split(" ")
        values.append(float(val))
        index_i.append(int(i))
        index_j.append(int(j))
        if(int(i)==109 and int(j)==218):
            break
        line = file1.readline()
    file1.close()

def p2():
    z=1
    file2 = open(porc2,'r')
    linea = file2.readline()
    while linea and z <110:
        val, i, j = linea.split(" ")
        values2.append(float(val))
        index_i2.append(int(i))
        index_j2.append(int(j))
        linea = file2.readline()
        z+=1
    file2.close()

p1()
p2()

j=0
for i in range(24200):
    if(i%219==0 and i!=219 and i!=0):
        index_i.insert(i,index_i2[j])
        index_j.insert(i,index_j2[j])
        values.insert(i,values2[j])
        if(index_i[i]==109 and index_j[i]==219):
            break
        j+=1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(1,2,3)
ax.set_title('Recongnition per frecuency')
ax.set_xlim([0,110])
ax.set_ylim([0,220])
ax.set_zlim([0,1])
surf = ax.plot_trisurf(index_i, index_j,values, cmap=cm.coolwarm)
ax.set_xlabel('index i')
ax.set_ylabel('index j')
ax.set_zlabel('classification %') #asi seria con latex r'$\gamma$'
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("grafica.pdf")
