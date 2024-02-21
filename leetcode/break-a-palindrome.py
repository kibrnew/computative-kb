class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n=len(palindrome)
        new=list(palindrome)
        
        if n==1:
            return ""
        f=False
        for i in range(n//2):
            if new[i]!="a":
                new[i]="a"
                f=True
                break 
                
        if not f:
            new[-1]="b"
        return "".join(new)
        
            
            
        
        