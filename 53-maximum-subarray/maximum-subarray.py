class Solution:
    def maxSubArray(self, nums):
        best = cur = nums[0]
        for x in nums[1:]:
            cur = cur + x if cur > 0 else x
            if cur > best:
                best = cur
        return best
