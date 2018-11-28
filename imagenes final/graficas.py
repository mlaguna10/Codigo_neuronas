import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

filepath='tulips.txt'
x1=[]
y1=[]

c=0
with open(filepath) as fp:
    line = fp.readline()
    while line:
        y1.append(float(line.split(' ')[1]))
        x1.append(float(line.split(' ')[5]))
        if(float(line.split(' ')[5])==0):
            c+=1
        line = fp.readline()

w,h = c,13
z = [[0 for x in range(w)] for y in range(h)]
t=0

for i in range(len(y1)):
    val = (i*10)%130
    z[val/10][t] = y1[i]
    if(val==120):
        t+=1

s = np.zeros(13)
for j in range(len(s)):
    s[j] = np.median(z[j])

file = open('tamanios',"r")
line = file.readline()
for k in range(len(x1)):
    if(k%13==0 and k!=0):
        line = file.readline()
    x1[k] = x1[k]/int(line)
file.close()

w,h = c,13
z2 = [[0 for x in range(w)] for y in range(h)]
t=0

for i in range(len(x1)):
    val = (i*10)%130
    z2[val/10][t] = x1[i]
    if(val==120):
        t+=1

s2 = np.zeros(13)
for j in range(len(s2)):
    s2[j] = np.median(z2[j])

j=0
fig = plt.figure()
plt.xlabel(r'$\vec{k}$ ($N_{y}$ units)')
plt.ylabel('% classification')
plt.plot(np.arange(0,0.53,0.53/13),s,linestyle='--', label='Median fit', color='red')
plt.grid()
while(j<len(x1)+1):
    plt.plot(x1[j:j+13],y1[j:j+13], alpha=.1)
    j+=13
plt.title("Tulips")
plt.legend()
plt.savefig('tulips.pdf')
plt.close()
