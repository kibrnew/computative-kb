class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=defaultdict(int)
        ans=0
        for t in time:
            i=-t%60
            ans+=d[i]
            d[t%60]+=1
        return ans
    