import numpy as np
import matplotlib.pyplot as plt

x = [10, 100, 1000, 10000, 100000, 1000000  ]
y1 = [368, 3284, 25651, 47111, 48369, 48397]
y2 = [306, 3190, 25494, 47076, 48364, 48400]

font = {'family': 'serif',
    'color':  'black',
    'weight': 'normal',
    'size': 15,
    }

fig = plt.figure()
ax = fig.add_subplot(121)
plt.scatter(np.log10(x),np.log10(y1),color='b')
plt.axhline(np.log10(y1[0]), color='gray', linestyle='-',label='$0.76\%$')
plt.axhline(np.log10(y1[1]), color='red', linestyle='-',label='$6.78\%$')
plt.axhline(np.log10(y1[2]), color='green', linestyle='-',label='$52.99\%$')
plt.axhline(np.log10(y1[3]), color='yellow', linestyle='-',label='$97.33\%$')
plt.axhline(np.log10(y1[4]), color='orange', linestyle='-',label='$99.93\%$')
plt.axhline(np.log10(y1[5]), color='pink', linestyle='-',label='$99.99\%$')
plt.xlabel('Real value limit (log scale)',fontsize=10)
plt.ylabel('Amount of frequencies under the limit (log scale)',fontsize=10)
plt.legend()
plt.title('Real value sections',fontdict=font)

ax = fig.add_subplot(122)
plt.scatter(np.log10(x),np.log10(y2),color='r')
plt.axhline(np.log10(y1[0]), color='gray', linestyle='-',label='$0.63\%$')
plt.axhline(np.log10(y1[1]), color='red', linestyle='-',label='$6.59\%$')
plt.axhline(np.log10(y1[2]), color='green', linestyle='-',label='$52.67\%$')
plt.axhline(np.log10(y1[3]), color='yellow', linestyle='-',label='$97.26\%$')
plt.axhline(np.log10(y1[4]), color='orange', linestyle='-',label='$99.92\%$')
plt.axhline(np.log10(y1[5]), color='pink', linestyle='-',label='$100\%$')
plt.xlabel('Imaginary value limit (log scale)',fontsize=10)
plt.ylabel('Amount of frequencies under the limit (log scale)',fontsize=10)
plt.legend()
plt.title('Imaginary value sections',fontdict=font)

plt.tight_layout()
plt.savefig('sections.pdf')
