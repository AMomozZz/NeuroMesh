import numpy as np
from itertools import combinations

def val(lst):
        # print(np.median(lst))
        #      O(n)           O(n logn) 
        return np.mean(lst) - np.median(lst) # O(n logn)

def Solution3(n, lst): # O(n^3 logn)
        maxVal = float('-inf')
        # O(n^2)
        for l in range(1, n + 1):
                for sub in combinations(lst, l):
                        maxVal = max(maxVal, val(sub))

        return maxVal

print(Solution3(4, [1,3,5,9]))