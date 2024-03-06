class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calc(target):
            ans=0
            for val in piles:
                ans+=ceil(val/target)

            return ans<=h
        
        l=1
        r=max(piles)

        while l<=r:
            mid=(l+r)//2
            
            if calc(mid):
                r=mid-1
            else:
                l=mid+1

        return l
