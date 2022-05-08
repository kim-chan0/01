# 2017013736 김찬영

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,3,5,10], label='price($)') # ([x-coordinate],[y-coordinate])
plt.xlabel('X-label') # labeling x-axis
plt.ylabel('Y-label') # labeling y-axis
plt.legend(loc=(1.0,1.0)) # Adding legend, label 'price($)' position is upper right

plt.show()

# Q) Change the position of label like the figures as below
# loc=(0,0), loc=(10),loc=(1,1)