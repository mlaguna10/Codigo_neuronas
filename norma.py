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
magnitude_spectrum = 20*np.log(np.abs(fshift))

phase = np.asarray(phase_spectrum).reshape(-1)
magnitude = np.asarray(magnitude_spectrum).reshape(-1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Magnitude Spectrum')
ax.scatter(np.arange(0,48400), np.arange(0,48400), magnitude, alpha=0.3)
ax.set_xlabel('index i')
ax.set_ylabel('index j')
ax.set_zlabel('magnitude')
ax.view_init(20, 35)
plt.tight_layout()
plt.savefig("magnitude_spectrum.pdf")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Phase Spectrum')
ax.scatter(np.arange(0,48400), np.arange(0,48400), phase, alpha=0.3)
ax.set_xlabel('index i')
ax.set_ylabel('index j')
ax.set_zlabel('phase')
ax.view_init(20, 35)
plt.tight_layout()
plt.savefig("phase_spectrum.pdf")

# plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title("Magnitud spectrum")
# plt.savefig("magnitude_spectrum3.pdf")
#
# plt.imshow(phase_spectrum, cmap = 'gray')
# plt.title("Phase spectrum")
# plt.savefig("phase_spectrum3.pdf")
