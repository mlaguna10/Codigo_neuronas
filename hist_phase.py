import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import cv2

# index_i = []
# index_j = []
# values = []
#
# file1 = open("porcentajes_modificado.txt",'r')
# file = open("porce_m.txt","w")
# line = file1.readline()
# while line:
#     val, i, j = line.split(" ")
#     if(int(j)>=110):
#         s=0
#     else:
#         file.write(str(val) + " " + str(i) + " " + str(j))
#     line = file1.readline()
# file1.close()
# file.close()

theta = []

def iter():
    for i in range(0,110):
        for j in range(0,110):
            print np.angle(dft[i][j])
            theta.append(np.angle(dft[i][j])[0])
    return theta

img = cv2.imread('gray_rose.jpg',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
iter()
fig = plt.figure()
plt.hist(theta, bins=50)
plt.savefig("hist_phase.pdf")
plt.close()
