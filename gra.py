import numpy as np
import matplotlib.pyplot as plt

p = [0.89040,0.99931,0.82857,0.42431,0.07928,0.07179,0.02872,0.04432,0.01918,0.06280,0.01659,0.17381,0.04226,0.10119]
k = [2,5,9,14,20,27,35,44,54,65,77,90,104,119]
f = [3,21,70,165,330,597,994,1561,2338,3373,4726,6447,8587,10634]

fig = plt.figure()

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 8,
        }

plt.title(r"Classification percentage given a $\vec{k}$",fontdict=font)
plt.xlabel(r'$\vec{k}$ limit',fontsize=10)
plt.ylabel(r'$\%$ classification',fontsize=10)
plt.plot(k,p)
plt.savefig("phase1.pdf")
plt.close()

fig = plt.figure()

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 8,
        }

plt.title(r"Classification percentage per amount of $f$ removed",fontdict=font)
plt.xlabel(r'amount of $f$ removed',fontsize=10)
plt.ylabel(r'$\%$ classification',fontsize=10)
plt.plot(f,p)
plt.savefig("phase2.pdf")
#plt.savefig("r.pdf")
