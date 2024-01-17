class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        s=sum(cardPoints[:k])
        ans=s
        for i in range(1,k+1):
            s+=cardPoints[-i]
            s-=cardPoints[k-i]
            ans=max(ans,s)
        return ans
            
            