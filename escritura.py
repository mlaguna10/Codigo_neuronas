import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


porc = 'porcentajes.txt'
porc2 = 'porcentajes2.txt'
porc3 = 'porcentajes_kvector.txt'
index_i = []
index_j = []
values = []
index_i2 = []
index_j2 = []
values2 = []

def grafica3D():
    #en la tesis se debe explicar que el paso es de 2 en 2.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(1,2,3)
    ax.set_title('Classification by each pair of frecuencies ')
    bins = np.arange(0,13)*9
    plt.xticks(bins, np.arange(0,13)*9,fontsize=7)
    bins = np.arange(0,13)*9
    plt.yticks(bins, np.arange(0,13)*9,fontsize=7)
    ax.set_zlim([0.91,0.98])
    surf = ax.plot_trisurf(index_i, index_j,values, cmap=cm.coolwarm)
    ax.set_xlabel('index i')
    ax.set_ylabel('index j')
    ax.set_zlabel('classification %')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.tight_layout()
    plt.savefig("N4_isolated_frec.pdf")

def p1(porc):
    #si estoy en grafica de vectork index i es el k limite y el index j es la cantidad de frecuencies que se hacen 0
    file1 = open(porc,'r')
    line = file1.readline()
    while line:
        val, i, j = line.split(" ")
        #si estoy en grafica isolated cambiar float por int en los indices
        values.append(float(val))
        index_i.append(float(i))
        index_j.append(float(j))
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

def grafica2D():
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 8,
        }

    fig = plt.figure()
    plt.subplot(221)
    plt.figtext(0.99, 0.01, r'*each vertical line is a new $|\vec{k}|$ upper limit', horizontalalignment='right', fontdict=font)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font,fontsize=5)
    plt.plot(index_i, values)

    plt.subplot(222)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$*',fontdict=font,fontsize=5)
    for i in range(50):
        plt.axvline(x=index_i[i], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[i])))
    #plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[0:50], values[0:50])

    plt.subplot(223)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$*',fontdict=font,fontsize=5)
    for i in range(50,100):
        plt.axvline(x=index_i[i], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[i])))
    #plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[50:100], values[50:100])

    plt.subplot(224)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$*',fontdict=font,fontsize=5)
    for i in range(100,155):
        plt.axvline(x=index_i[i], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[i])))
    #plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[100:156], values[100:156])

    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    fig.suptitle('Classification by Frequency Filter',fontdict=font, fontsize=10)
    plt.savefig("Frequency_filter.pdf")
    plt.close()

p1(porc3)
grafica2D()

#p1("porcentajes_modificado.txt")
#grafica3D()
