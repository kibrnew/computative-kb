class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans=float("inf")
        ind={}
        for i,val in enumerate(cards) :
            if val in ind:
                ans=min(ans,i-ind[val]+1)
            ind[val]=i
        if ans==float("inf"):
            return -1
        return ans
            