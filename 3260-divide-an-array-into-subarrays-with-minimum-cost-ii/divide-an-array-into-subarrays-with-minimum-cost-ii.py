from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        need = k - 1
        
        sl = SortedList(nums[1:dist+2])
        cur = sum(sl[:need])
        ans = cur
        
        for i in range(2, n - dist):
            out = nums[i-1]
            idx = sl.bisect_left(out)
            if idx < need:
                cur -= out
                if need < len(sl):
                    cur += sl[need]
            sl.remove(out)
            
            new = nums[i+dist]
            idx = sl.bisect_left(new)
            if idx < need:
                cur += new
                if need-1 < len(sl):
                    cur -= sl[need-1]
            sl.add(new)
            
            ans = min(ans, cur)
        
        return ans + nums[0]