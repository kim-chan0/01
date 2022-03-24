# 2017013736 김찬영

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,3,5,10], label='Price ($)')   # ([x-coordinate],[y-coordinate])
plt.plot([1,2,3,4],[3,5,9,7], label='Demand (#)')   # ([x-coordinate],[y-coordinate])
plt.xlabel('X-Axis')    # labeling x-axis
plt.ylabel('Y-Axis')    # labeling y-axis
# plt.legend(loc='best')
plt.legend(loc='best', ncol=2)  # location is best, 2 column

plt.show()