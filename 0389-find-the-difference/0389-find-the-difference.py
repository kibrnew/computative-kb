class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count=Counter(s)
        
        for a in t :
            if count[a]==0:
                return a
            else:
                count[a]-=1
        