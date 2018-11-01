import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


porc = 'porcentajes.txt'
porc2 = 'porcentajes2.txt'
porc3 = 'porcentajes_kvector.txt'
porc4 = 'porcentajes_phase_change_altas.txt'
porc5 = 'porcentajes_phase_change_bajas.txt'
porc6 = 'amplitude.txt'
index_i = []
index_j = []
values1 = []
values2 = []
values3 = []
values4 = []
values5 = []

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
        val_rose, val_tuli, val_gira, val_diente, val_marg, i, j = line.split(" ")
        #si estoy en grafica isolated cambiar float por int en los indices
        values1.append(float(val_rose))
        values2.append(float(val_tuli))
        values3.append(float(val_gira))
        values4.append(float(val_diente))
        values5.append(float(val_marg))
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
        'color':  'black',
        'weight': 'normal',
        'size': 8,
        }

    fig = plt.figure()
    #plt.figtext(0.99, 0.01, r'*each vertical line is a new $|\vec{k}|$ upper limit', horizontalalignment='right', fontdict=font)
    #plt.subplot(121)
    plt.xlabel(r'number of frecuencies changed')
    plt.ylabel('% classification')
    axes = plt.gca()
    #axes.set_xlim([0,120])
    plt.title(r'classification percentage by $|\vec{k}|$ in amplitude information',fontdict=font,fontsize=5)
    plt.plot(index_j, values1,linewidth=0.01, label="Rose")
    #plt.axvline(index_i[4], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_j[4])))
    plt.plot(index_j, values2, linewidth=0.01, label='Tulip')
    plt.plot(index_j, values3, linewidth=0.01, label='Sunflower')
    plt.plot(index_j, values4, linewidth=0.01, label='Dandelion')
    plt.plot(index_j, values5, linewidth=0.01, label='Daisy')
    #rosas, tulipanes, sunflowers, dandelion, daisy

    #plt.subplot(122)
    # plt.xlabel(r'$|\vec{k}|$')
    # plt.ylabel('% classification')
    # plt.title(r'classification percentage by $|\vec{k}|$ in phase information',fontdict=font,fontsize=5)
    # plt.plot(index_i2, values12, color="b",linewidth=0.01, label="Filtro pasa bajas")
    #plt.axvline(index_i2[1], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_j2[1])))

    plt.legend(loc=6, prop={'size': 4})
    plt.tight_layout()
    plt.savefig("Frequency_filter.pdf")
    plt.close()

    # plt.subplot(222)
    # plt.xlabel(r'$|\vec{k}|$')
    # plt.ylabel('% classification')
    # plt.title(r'classification percentage by $|\vec{k}|$*',fontdict=font,fontsize=5)
    # for i in range(50):
    #     plt.axvline(x=index_i[i], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[i])))
    # #plt.legend(loc=2, prop={'size': 4})
    # plt.plot(index_i[0:50], values[0:50])
    #
    # plt.subplot(223)
    # plt.xlabel(r'$|\vec{k}|$')
    # plt.ylabel('% classification')
    # plt.title(r'classification percentage by $|\vec{k}|$*',fontdict=font,fontsize=5)
    # for i in range(50,100):
    #     plt.axvline(x=index_i[i], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[i])))
    # #plt.legend(loc=2, prop={'size': 4})
    # plt.plot(index_i[50:100], values[50:100])
    #
    # plt.subplot(224)
    # plt.xlabel(r'$|\vec{k}|$')
    # plt.ylabel('% classification')
    # plt.title(r'classification percentage by $|\vec{k}|$*',fontdict=font,fontsize=5)
    # for i in range(100,155):
    #     plt.axvline(x=index_i[i], color='grey', linestyle='--',linewidth=0.01, label=str('%.2f'%(index_i[i])))
    # #plt.legend(loc=2, prop={'size': 4})
    # plt.plot(index_i[100:156], values[100:156])

p1(porc6)
grafica2D()


#p1("porcentajes_modificado.txt")
#grafica3D()
