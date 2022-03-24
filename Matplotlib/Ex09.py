# 2017013736 김찬영

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)  # (start, stop, num)
y = np.exp(x)   # y is exponential function of x

plt.plot(x,y)
# plt.yscale('linear') --> y scale is linear
plt.yscale('log')   # y scale is log

plt.show()