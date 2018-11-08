import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

img = cv2.imread('gray_rose.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
phase_spectrum = np.angle(fshift)
magnitude_spectrum = np.log(np.abs(fshift))

phase = np.asarray(phase_spectrum).reshape(-1)
magnitude = np.asarray(magnitude_spectrum).reshape(-1)

font = {'family': 'serif',
    'color':  'black',
    'weight': 'normal',
    'size': 12,
    }

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Magnitude spectrum centered (log scale)', fontdict=font)
magnitude = np.reshape(magnitude, (220,220))
u = np.arange(0,220)
v = np.arange(0,220)
U, V = np.meshgrid(u,v)
surf = ax.plot_surface(U,V,magnitude, cmap=cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('frequency u')
ax.set_ylabel('frequency v')
ax.set_zlabel('magnitude')
plt.tight_layout()
plt.savefig("magnitude_spectrum.pdf")
plt.close()
# ax.view_init(20, 35)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Phase spectrum centered', fontdict=font)
phase = np.reshape(phase, (220,220))
u = np.arange(0,220)
v = np.arange(0,220)
U, V = np.meshgrid(u,v)
surf = ax.plot_surface(U,V,phase, cmap=cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('frequency u')
ax.set_ylabel('frequency v')
ax.set_zlabel('phase')
plt.tight_layout()
plt.savefig("phase_spectrum.pdf")
plt.close()

plt.imshow(magnitude_spectrum)
plt.title("Magnitude spectrum", fontdict=font)
plt.xlabel("frequency u")
plt.ylabel("frequency v")
plt.savefig("magnitude_spectrum3.pdf")

plt.imshow(phase_spectrum)
plt.title("Phase spectrum", fontdict=font)
plt.xlabel("frequency u")
plt.ylabel("frequency v")
plt.savefig("phase_spectrum3.pdf")
