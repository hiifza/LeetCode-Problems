class DSU:
    def __init__(self,n):
        self.p=list(range(n))
        self.r=[0]*n

    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x

    def union(self,a,b):
        pa=self.find(a)
        pb=self.find(b)
        if pa==pb:
            return False
        if self.r[pa]<self.r[pb]:
            pa,pb=pb,pa
        self.p[pb]=pa
        if self.r[pa]==self.r[pb]:
            self.r[pa]+=1
        return True


class Solution:
    def maxStability(self, n, edges, k):

        def can(x):
            dsu=DSU(n)
            upgrades=0
            used=0

            # mandatory edges
            for u,v,s,m in edges:
                if m:
                    if s<x:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used+=1

            normal=[]
            upgrade=[]

            for u,v,s,m in edges:
                if m: 
                    continue
                if s>=x:
                    normal.append((u,v))
                elif s*2>=x:
                    upgrade.append((u,v))

            for u,v in normal:
                if dsu.union(u,v):
                    used+=1

            for u,v in upgrade:
                if used==n-1:
                    break
                if upgrades==k:
                    break
                if dsu.union(u,v):
                    upgrades+=1
                    used+=1

            return used==n-1

        lo,hi=0,2*10**5
        ans=-1

        while lo<=hi:
            mid=(lo+hi)//2
            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1

        return ans