class Solution:
    
    def lcp(self, a, b):
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        return i

    def longestCommonPrefix(self, words):
        n = len(words)
        
        if n == 1:
            return [0]
        
        lcp = [0]*(n-1)
        for i in range(n-1):
            lcp[i] = self.lcp(words[i], words[i+1])
        
        pref = [0]*(n-1)
        pref[0] = lcp[0]
        for i in range(1,n-1):
            pref[i] = max(pref[i-1], lcp[i])
        
        suff = [0]*(n-1)
        suff[-1] = lcp[-1]
        for i in range(n-3,-1,-1):
            suff[i] = max(suff[i+1], lcp[i])
        
        ans = [0]*n
        
        for i in range(n):
            best = 0
            
            if i-2 >= 0:
                best = max(best, pref[i-2])
            
            if i+1 <= n-2:
                best = max(best, suff[i+1])
            
            if 0 < i < n-1:
                best = max(best, self.lcp(words[i-1], words[i+1]))
            
            ans[i] = best
        
        return ans