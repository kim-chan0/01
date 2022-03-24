# 2017013736 김찬영

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,3,5,10])   # ([x-coordinate],[y-coordinate])

plt.xlabel('X-Axis')    # labeling x-axis
plt.ylabel('Y-Axis')    # labeling y-axis
plt.axis([0,5,0,20])    # range : [xmin, xmax, ymin, ymax]

plt.show()