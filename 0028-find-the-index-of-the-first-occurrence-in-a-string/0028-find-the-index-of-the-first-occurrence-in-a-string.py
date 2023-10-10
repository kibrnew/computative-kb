class Solution:
    def strStr(self, heystack: str, needle: str) -> int:
        lh=len(heystack)
        lt=len(needle)
        if lh<lt:
            return -1
        target=0
        temp=0
       
        for i in range(lt):
            p=lt-i-1
            target+=(26**p)*(ord(needle[i])-96)
            temp+=(26**p)*(ord(heystack[i])-96)
        if target==temp:
            return 0
        
        for i in range(lt,lh):
            pi=i-lt
            
            temp-=(26**(lt-1))*(ord(heystack[pi])-96)
            temp*=26
            temp+=(ord(heystack[i])-96)
            if temp==target:
                return (pi+1)
        return -1
            
            
        