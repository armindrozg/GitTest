# Computer speed test

import numpy as np
import time

n = 100

tic = time.clock()
for i in range(n):
    a = np.random.rand(1000, 1000)

    ainv = np.linalg.inv(a)
toc = time.clock()
print('Time: ', (toc-tic)/n, ' s')