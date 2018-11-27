import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

filepath='daisy.txt'
x=[]
y=[]

with open(filepath) as fp:
    line = fp.readline()
    while line:
        y.append(float(line.split(' ')[4]))
        x.append(float(line.split(' ')[5]))
        line = fp.readline()

z = np.zeros(13)
c=0
for i in range(len(y)):
    val = (i*10)%130
    z[val/10] = z[val/10] + y[i]
    if(val==0):
        c+=1

average = z/c

j=0
fig = plt.figure()
plt.xlabel(r'$\vec{k}$')
plt.ylabel('% classification')
plt.plot(np.arange(0,130,10),average,linestyle='--', label='Average fit', color='red')
plt.axvline(0,color='blue', linestyle='--',linewidth=0.05, label=r'$\vec{k}=0$')
plt.axvline(5,color='red', linestyle='--',linewidth=0.05, label=r'$\vec{k}=5$')
plt.axvline(10,color='black', linestyle='--',linewidth=0.05, label=r'$\vec{k}=10$')
while(j<len(x)+1):
    plt.plot(x[j:j+13],y[j:j+13], alpha=.1)
    j+=13
plt.title("Daisy")
plt.legend()
plt.savefig('daisy.pdf')
plt.close()
