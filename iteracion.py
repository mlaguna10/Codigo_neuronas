import numpy as np
import os
import time
start = time.time()

for i in range(24200):
    os.system('python DFT.py > output.tx')
    #os.system('python escritura.py')

end = time.time()
print(end - start)
