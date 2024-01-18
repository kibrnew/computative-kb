class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l=0
        n=len(answerKey)
        count=Counter()
        ans=0
        for r in range(n):
            count[answerKey[r]]+=1
            while max(count.values())+k<r-l+1:
                count[answerKey[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
        