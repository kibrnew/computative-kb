class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count=Counter(s)
        ans=0
        off=0
        for key,val in count.items():
            ans+=2*(val//2)
            off+=val%2
        if off:
            ans+=1
        return ans
        