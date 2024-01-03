class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=[]
        for val in s:
            if val.isalnum():
                val=val.lower()
                ans.append(val)
            
                
        res="".join(ans)
        return res==res[::-1]