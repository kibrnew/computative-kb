class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:


    
        dp=[[0]*(n+1) for _ in range(m+1)]
        temp=[[0]*(n+1) for _ in range(m+1)]
        for val in strs:
            one=val.count("1")
            zero=val.count("0")
            for i in range(m+1):
                for j in range(n+1):
                    temp[i][j]=dp[i][j]
                    if i>=zero and j>=one:
                        temp[i][j]=max(temp[i][j],dp[i-zero][j-one]+1)
                    
                    




            dp,temp=temp,dp

        return dp[m][n]

        


