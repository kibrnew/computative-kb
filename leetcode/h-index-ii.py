class Solution:
    def hIndex(self, citations: List[int]) -> int:

        r=max(citations)
        l=0
        while l<=r:
            mid=(l+r)//2
            if mid<=len(citations)-bisect_left(citations,mid):
                l=mid+1
            else:
                r=mid-1
        return r
            
        