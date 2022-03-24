# 2017013736 김찬영

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)   # (start, stop, num)
y = x ** 3  # value of y is x^3

plt.plot(x,y)
plt.xscale('symlog')    # 'symlog' is enable to expression of negative value

plt.show()