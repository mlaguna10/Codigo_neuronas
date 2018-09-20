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
    bins = np.arange(0,12)*20
    plt.yticks(bins, np.arange(0,12)*20,fontsize=7)
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
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.plot(index_i, values)

    plt.subplot(222)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.axvline(x=index_i[0], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[0])))
    plt.axvline(x=index_i[1], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[1])))
    plt.axvline(x=index_i[2], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[2])))
    plt.axvline(x=index_i[3], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[3])))
    plt.axvline(x=index_i[4], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[4])))
    plt.axvline(x=index_i[5], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[5])))
    plt.axvline(x=index_i[6], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[6])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[0:7], values[0:7])


    plt.subplot(223)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.axvline(x=index_i[7], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[7])))
    plt.axvline(x=index_i[8], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[8])))
    plt.axvline(x=index_i[9], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[9])))
    plt.axvline(x=index_i[10], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[10])))
    plt.axvline(x=index_i[11], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[11])))
    plt.axvline(x=index_i[12], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[12])))
    plt.axvline(x=index_i[13], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[13])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[7:14], values[7:14])

    plt.subplot(224)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.axvline(x=index_i[14], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[14])))
    plt.axvline(x=index_i[15], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[15])))
    plt.axvline(x=index_i[16], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[16])))
    plt.axvline(x=index_i[17], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[17])))
    plt.axvline(x=index_i[18], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[18])))
    plt.axvline(x=index_i[19], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[19])))
    plt.axvline(x=index_i[20], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[20])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[14:21], values[14:21])

    plt.tight_layout()
    plt.savefig("magnitude_filter_1.pdf")
    plt.close()

    fig = plt.figure()
    plt.subplot(221)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.axvline(x=index_i[21], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[21])))
    plt.axvline(x=index_i[22], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[22])))
    plt.axvline(x=index_i[23], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[23])))
    plt.axvline(x=index_i[24], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[24])))
    plt.axvline(x=index_i[25], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[25])))
    plt.axvline(x=index_i[26], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[16])))
    plt.axvline(x=index_i[27], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[27])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[21:28], values[21:28])

    plt.subplot(222)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.axvline(x=index_i[28], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[28])))
    plt.axvline(x=index_i[29], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[29])))
    plt.axvline(x=index_i[30], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[30])))
    plt.axvline(x=index_i[31], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[31])))
    plt.axvline(x=index_i[32], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[32])))
    plt.axvline(x=index_i[33], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[33])))
    plt.axvline(x=index_i[34], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[34])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[28:35], values[28:35])

    plt.subplot(223)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.axvline(x=index_i[35], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[35])))
    plt.axvline(x=index_i[36], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[36])))
    plt.axvline(x=index_i[37], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[37])))
    plt.axvline(x=index_i[38], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[38])))
    plt.axvline(x=index_i[39], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[39])))
    plt.axvline(x=index_i[40], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[40])))
    plt.axvline(x=index_i[41], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[41])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[35:42], values[35:42])

    plt.subplot(224)
    plt.xlabel(r'$|\vec{k}|$')
    plt.ylabel('% classification')
    plt.title(r'classification percentage by $|\vec{k}|$',fontdict=font)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.axvline(x=index_i[42], color='black', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[42])))
    plt.axvline(x=index_i[43], color='b', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[43])))
    plt.axvline(x=index_i[44], color='g', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[44])))
    plt.axvline(x=index_i[45], color='r', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[45])))
    plt.axvline(x=index_i[46], color='y', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[46])))
    plt.axvline(x=index_i[47], color='gray', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[47])))
    plt.axvline(x=index_i[48], color='pink', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[48])))
    plt.legend(loc=2, prop={'size': 4})
    plt.plot(index_i[42:49], values[42:49])

    plt.tight_layout()
    plt.savefig("magnitude_filter_2.pdf")
    plt.close()

p1(porc3)
grafica2D()

#p2()
#grafica3D()
