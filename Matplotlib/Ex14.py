# 2017013736 김찬영

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g-.')    #(1st curve, 2nd curve, 3rd curve), -. means dash-dot line
plt.show()