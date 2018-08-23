#(Extra): http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php
#Creditos: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess

N = 220

def cut_off_frec(frec):
    return frec

img = cv2.imread('gray_rose.jpg',0)
for i in range(1):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft = cut_off_frec(dft)
    dft_shift = np.fft.fftshift(dft)
    f_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    fig = plt.figure()
    fig.set_size_inches(3.5,3.5)
    plt.imshow(img_back, cmap = 'gray')
    plt.xticks([]), plt.yticks([])
    plt.savefig('frec_' + str(i) + ".png")
    os.system("python scripts/label_image.py --image frec_" + str(i) + ".png")
    process = subprocess.Popen(["roses (score=0.98794)"], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    print(result)
