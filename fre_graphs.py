import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import sys
from matplotlib import colors

img = cv2.imread('gray_rose.jpg',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
reales = []
complejos = []
for i in range(0,220):
    for j in range(0,220):
        r,c = dft[i][j]
        reales.append(r)
        complejos.append(c)

def img_real_frec(y,real):
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    if(real):
        fig = plt.figure()
        x = np.arange(48400)

        plt.subplot(111)
        plt.plot(x,y,linestyle='-')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.legend(loc=2, prop={'size': 4})
        plt.title("Real part value per frecuency",fontdict=font)
        plt.xlabel('Frecuencies',fontsize=7)
        plt.ylabel('Real part value',fontsize=7)

        plt.savefig("real_frec.pdf")
    else:
        fig = plt.figure()
        x = np.arange(48400)

        plt.subplot(111)
        plt.plot(x,y,linestyle='-')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.legend(loc=2, prop={'size': 4})
        plt.title("Imaginary part value per frecuency",fontdict=font)
        plt.xlabel('Frecuencies',fontsize=7)
        plt.ylabel('Imaginary part value',fontsize=7)

        plt.savefig("imaginary_frec.pdf")

def img_real_sections(y,real):
    x = np.arange(48400)
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 5,
        }
    if(real):
        fig = plt.figure()
        plt.subplot(321)
        plt.ylim(-100,100)
        y = np.array(y)
        #print y[np.abs(y)<10]
        plt.scatter(x[np.abs(y)<10],y[np.abs(y)<10],s=1,c='red',label=r'$368 (0.76 \%)$')
        plt.scatter(x[np.abs(y)>=10],y[np.abs(y)>=10],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec real part value less than 10",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Real part value',fontsize=5)

        plt.subplot(322)
        plt.ylim(-1000,1000)
        #print np.shape(y[np.abs(y)<100])
        plt.scatter(x[np.abs(y)<100],y[np.abs(y)<100],s=1,c='red',label=r'$3284 (6.78 \%)$')
        plt.scatter(x[np.abs(y)>=100],y[np.abs(y)>=100],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec real part value less than 100",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Real part value',fontsize=5)

        plt.subplot(323)
        plt.ylim(-10000,10000)
        #print np.shape(y[np.abs(y)<1000])
        plt.scatter(x[np.abs(y)<1000],y[np.abs(y)<1000],s=1,c='red',label=r'$25651 (52.99\%)$')
        plt.scatter(x[np.abs(y)>=1000],y[np.abs(y)>=1000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec real part value less than 1000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Real part value',fontsize=5)

        plt.subplot(324)
        plt.ylim(-100000,100000)
        #print np.shape(y[np.abs(y)<10000])
        plt.scatter(x[np.abs(y)<10000],y[np.abs(y)<10000],s=1,c='red',label=r'$ 47111 (97.33 \%)$')
        plt.scatter(x[np.abs(y)>=10000],y[np.abs(y)>=10000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec real part value less than 10.000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Real part value',fontsize=5)

        plt.subplot(325)
        plt.ylim(-1000000,1000000)
        #print np.shape(y[np.abs(y)<100000])
        plt.scatter(x[np.abs(y)<100000],y[np.abs(y)<100000],s=1,c='red',label=r'$48369 (99.93 \%)$')
        plt.scatter(x[np.abs(y)>=100000],y[np.abs(y)>=100000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec real part value less than 100.000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Real part value',fontsize=5)

        plt.subplot(326)
        plt.ylim(-10000000,10000000)
        #print np.shape(y[np.abs(y)<1000000])
        plt.scatter(x[np.abs(y)<1000000],y[np.abs(y)<1000000],s=1,c='red',label=r'$48397 (99.99 \%)$')
        plt.scatter(x[np.abs(y)>=1000000],y[np.abs(y)>=1000000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec real part value less than 1.000.000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Real part value',fontsize=5)

        plt.tight_layout()

        plt.savefig("real_sections.pdf")
    else:
        fig = plt.figure()
        plt.subplot(321)
        plt.ylim(-100,100)
        y = np.array(y)
        plt.scatter(x[np.abs(y)<10],y[np.abs(y)<10],s=1,c='red',label=r'$306 (0.63 \%)$')
        plt.scatter(x[np.abs(y)>=10],y[np.abs(y)>=10],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec imaginary part value less than 10",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Imaginary part value',fontsize=5)

        plt.subplot(322)
        plt.ylim(-1000,1000)
        plt.scatter(x[np.abs(y)<100],y[np.abs(y)<100],s=1,c='red',label=r'$3190 (6.59 \%)$')
        plt.scatter(x[np.abs(y)>=100],y[np.abs(y)>=100],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec imaginary part value less than 100",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Imaginary part value',fontsize=5)

        plt.subplot(323)
        plt.ylim(-10000,10000)
        plt.scatter(x[np.abs(y)<1000],y[np.abs(y)<1000],s=1,c='red',label=r'$25494 (52.67\%)$')
        plt.scatter(x[np.abs(y)>=1000],y[np.abs(y)>=1000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec imaginary part value less than 1000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Imaginary part value',fontsize=5)

        plt.subplot(324)
        plt.ylim(-100000,100000)
        plt.scatter(x[np.abs(y)<10000],y[np.abs(y)<10000],s=1,c='red',label=r'$ 47076 (97.26 \%)$')
        plt.scatter(x[np.abs(y)>=10000],y[np.abs(y)>=10000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec imaginary part value less than 10.000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Imaginary part value',fontsize=5)

        plt.subplot(325)
        plt.ylim(-1000000,1000000)
        plt.scatter(x[np.abs(y)<100000],y[np.abs(y)<100000],s=1,c='red',label=r'$48364 (99.92 \%)$')
        plt.scatter(x[np.abs(y)>=100000],y[np.abs(y)>=100000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec imaginary part value less than 100.000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Imaginary part value',fontsize=5)

        plt.subplot(326)
        plt.ylim(-10000000,10000000)
        plt.scatter(x[np.abs(y)<1000000],y[np.abs(y)<1000000],s=1,c='red',label=r'$48400 (100 \%)$')
        plt.scatter(x[np.abs(y)>=1000000],y[np.abs(y)>=1000000],s=1,c='gray')
        plt.plot(np.arange(48400),np.zeros(48400),color='black',linewidth=0.01,label='zero line')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.title("Frec imaginary part value less than 1.000.000",fontdict=font)
        plt.legend(loc=2, prop={'size': 4})
        plt.xlabel('Frecuencies',fontsize=5)
        plt.ylabel('Imaginary part value',fontsize=5)

        plt.tight_layout()

        plt.savefig("imaginary_sections.pdf")

def img_real_hist(y,real):
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    if(real):
        fig = plt.figure()
        plt.subplot(111)
        y = np.array(y)
        bins = np.arange(0,7)
        plt.xticks(bins, [r"$10^%s$" % i for i in bins])
        plt.hist(np.log10(abs(y)),log=True, bins='auto')
        plt.axhline(10,c='b',linewidth=0.1)
        plt.axhline(100,c='b',linewidth=0.1)
        plt.axhline(1000,c='b',linewidth=0.1)
        plt.axhline(1,c='b',linewidth=0.1)
        plt.xlabel('Real part value')
        plt.ylabel('Amount of frecuencies')
        plt.title("Histogram of real part values per frecuency",fontdict=font)

        plt.savefig("real_hist.pdf")
    else:
        fig = plt.figure()
        plt.subplot(111)
        y = np.array(y)
        bins = np.arange(0,10)
        plt.xticks(bins, [r"$10^%s$" % i for i in bins])
        y[0] = 10**-10
        y[110] = 10**-10
        plt.hist(np.log10(abs(y)),log=True, bins='auto')
        plt.axhline(10,c='b',linewidth=0.1)
        plt.axhline(100,c='b',linewidth=0.1)
        plt.axhline(1000,c='b',linewidth=0.1)
        plt.axhline(1,c='b',linewidth=0.1)
        plt.xlabel('Imaginary part value')
        plt.ylabel('Amount of frecuencies')
        plt.title("Histogram of imaginary part values per frecuency",fontdict=font)

        plt.savefig("imaginary_hist.pdf")

#img_real_frec(reales,True)
#img_real_frec(complejos,False)

#img_real_sections(reales,True)
#img_real_sections(complejos,False)

#img_real_hist(reales,True)
#img_real_hist(complejos,False)
