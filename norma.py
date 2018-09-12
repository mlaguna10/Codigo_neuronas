import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img = cv2.imread('gray_rose.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
phase_spectrum = np.angle(fshift)
print type(fshift), np.shape(fshift)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title("Magnitud spectrum")
# plt.savefig("magnitude_spectrum.pdf")
#
# plt.imshow(phase_spectrum, cmap = 'gray')
# plt.title("Phase spectrum")
# plt.savefig("phase_spectrum.pdf")
