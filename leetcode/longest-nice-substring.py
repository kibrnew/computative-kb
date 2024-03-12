class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        n=len(s)
        def check(temp):
            stor=set(temp)
            for val in temp:
                if val.swapcase() not in stor:
                    return False
            return True
        ans=""
        for i in range(2,n+1):
            for j in range(n-i+1):
                cur=s[j:j+i]
                if check(cur):
                    ans=cur
                    break
        return ans
                    
                
            
        