# 2017013736 김찬영

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [2.0,3.0,5.0,10.0], color='limegreen')    # ([x-coordinate],[y-coordinate]), limegreen color
plt.plot([1,2,3,4], [2.0,2.8,4.3,6.5], color='violet')    # ([x-coordinate],[y-coordinate]), violet color
plt.plot([1,2,3,4], [2.0,2.5,3.3,4.5], color='dodgerblue')    # ([x-coordinate],[y-coordinate]), dodgerblue color
plt.xlabel('X-Axis')    # labeling x-axis
plt.ylabel('Y-Axis')    # labeling y-axis

plt.show()