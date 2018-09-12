import numpy as np
import os
import time
start = time.time()

for i in range(6050):
    os.system('python DFT.py > output.txt')
    #os.system('python escritura.py')

end = time.time()
print(end - start)
