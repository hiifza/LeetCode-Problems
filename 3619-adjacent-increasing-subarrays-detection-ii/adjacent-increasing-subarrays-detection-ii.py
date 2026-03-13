class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        
        prev = 0
        curr = 1
        ans = 0
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                ans = max(ans, curr // 2)
                ans = max(ans, min(prev, curr))
                prev = curr
                curr = 1
        
        ans = max(ans, curr // 2)
        ans = max(ans, min(prev, curr))
        
        return ans