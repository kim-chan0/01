# 2017013736 김찬영

# 11a + 7b + 8c - 4d - 2e = 23
# 9a - 8b + 5c + 11d -4e = 32
# a + 13b -10c + 2d + e = 10
# -3a + b + c - d + 2e = 8
# 21a - 7b -5c + d + e = 31

import numpy as np

n = int(input('n = ')) # Input the value of n.
A,B = [], [] # Create empty list 'A,B'.
for x in range(n): # Repeat n.
    a = list(map(int, input().split())) # Create a list 'a', input the value.
    if len(a) != n: break # If length of list 'a' is different with n, break.
    A.append(a)  # Append a to 'A'

if len(a) == n: # If length of list 'a' is same n,
    B = list(map(int, input().split())) # Create a list 'B', input the value.

try:
    x = np.linalg.solve(A, B) # Solve the linear algebra.
    print(x)
except:
    print('error') # If there is an error, print 'error'