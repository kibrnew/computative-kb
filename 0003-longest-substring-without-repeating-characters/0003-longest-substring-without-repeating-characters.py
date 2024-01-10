class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        left=0
        n=len(s)
        visited=set()
        for right in range(n):
            
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
                
            visited.add(s[right])
            ans=max(ans,right-left+1)
        return ans 
            
        