from collections import Counter

class Solution:
    def findSmallestInteger(self, nums, value):
        count = Counter()
        
        for num in nums:
            r = num % value
            count[r] += 1
        
        mex = 0
        
        while True:
            r = mex % value
            if count[r] == 0:
                return mex
            count[r] -= 1
            mex += 1