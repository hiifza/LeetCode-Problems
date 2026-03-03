class Solution:
    def findKthBit(self, n, k):
        flip = 0
        
        while n > 1:
            mid = 1 << (n - 1)  # 2^(n-1)
            
            if k == mid:
                return str(1 ^ flip)
            
            if k > mid:
                k = (1 << n) - k
                flip ^= 1
            
            n -= 1
        
        return str(flip)