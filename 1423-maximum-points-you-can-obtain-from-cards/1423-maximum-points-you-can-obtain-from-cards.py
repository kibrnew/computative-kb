class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=cardPoints[:k]
        leng=len(cardPoints)
        right=cardPoints[-k:]
        temp=right+left
        cur=sum(right)
        ans=set([cur])
        for i in range(k):
            cur-=temp[i] 
            cur+=temp[i+k]
            ans.add(cur)
        return max(ans)
            
            