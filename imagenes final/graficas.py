import numpy as np
import matplotlib.pyplot as plt

filepath='tulips.txt'
x=[]
y=[]

with open(filepath) as fp:
    line = fp.readline()
    while line:
        y.append(float(line.split(' ')[1]))
        x.append(float(line.split(' ')[5]))
        line = fp.readline()

s1,s2,s3=0,0,0
c=0
for i in range(len(y)):
    if(x[i]==0):
        s1+=y[i]
        c+=1
    elif(x[i]==5):
        s2+=y[i]
    else:
        s3+=y[i]

y1 = s1/c
y2 = s2/c
y3 = s3/c

j=0
fig = plt.figure()
plt.xlabel(r'$\vec{k}$')
plt.ylabel('% classification')
plt.plot([0,5,10],[y1,y2,y3],linestyle='--', label='Average fit')
plt.axvline(0,color='blue', linestyle='--',linewidth=0.05, label=r'$\vec{k}=0$')
plt.axvline(5,color='red', linestyle='--',linewidth=0.05, label=r'$\vec{k}=5$')
plt.axvline(10,color='black', linestyle='--',linewidth=0.05, label=r'$\vec{k}=10$')
while(j<len(x)/3):
    plt.plot(x[j:j+3],y[j:j+3], alpha=.2)
    j+=3
plt.legend()
plt.savefig('tulips.pdf')
