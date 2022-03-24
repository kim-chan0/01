# 2017013736 김찬영

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [2.0,3.0,5.0,10.0], 'r')    # ([x-coordinate],[y-coordinate]), red color
plt.plot([1,2,3,4], [2.0,2.8,4.3,6.5], 'g')    # ([x-coordinate],[y-coordinate]), green color
plt.plot([1,2,3,4], [2.0,2.5,3.3,4.5], 'b')    # ([x-coordinate],[y-coordinate]), blue color
plt.xlabel('X-Axis')    # labeling x-axis
plt.ylabel('Y-Axis')    # labeling y-axis

plt.show()