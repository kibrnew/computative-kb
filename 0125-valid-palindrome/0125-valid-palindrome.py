class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=[]
        for val in s:
            val=val.lower()
            if ord("a")<=ord(val)<=ord("z") or ord("0")<=ord(val)<=ord("9"):
                ans.append(val)
                
        res="".join(ans)
        return res==res[::-1]