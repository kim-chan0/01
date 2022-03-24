# 2017013736 김찬영

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,3,5,10], label='price($)') # ([x-coordinate],[y-coordinate])
plt.xlabel('X-label') # labeling x-axis
plt.ylabel('Y-label') # labeling y-axis
plt.legend() # Adding legend

plt.show()