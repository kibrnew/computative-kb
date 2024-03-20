class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        ans=[]
        n=len(weights)
        for i in range(n-1):
            ans.append(weights[i]+weights[i+1])

        ans.sort()

        mini=sum(ans[:k-1])
        maxi=sum(ans[n-k:])

        # print(ans)

        return maxi-mini
