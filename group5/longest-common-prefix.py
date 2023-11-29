class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        left=strs[0]
        right=strs[-1]
        n=min(len(right),len(left))
        if n==0:
            return""
        for i in range(n):
            if left[i]!=right[i]:
                break     
        else:
            i+=1
        return left[:i]
                    
                    
            
            
        