import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

index_i = []
index_j = []
values = []

file1 = open("porcentajes_modificado.txt",'r')
file = open("porce_m.txt","w")
line = file1.readline()
while line:
    val, i, j = line.split(" ")
    if(int(j)>=110):
        s=0
    else:
        file.write(str(val) + " " + str(i) + " " + str(j))
    line = file1.readline()
file1.close()
file.close()
