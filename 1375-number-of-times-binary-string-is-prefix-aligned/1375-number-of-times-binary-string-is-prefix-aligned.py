class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n=len(flips)
        maxi=0
        ans=0
        for i in range(n) :
            maxi=max(maxi,flips[i])
            if i+1==maxi:
                ans+=1
        return ans
        