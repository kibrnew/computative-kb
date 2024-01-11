class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ans=0
        count=Counter()
        left=0
        for right in range(n):
            count[s[right]]+=1
            while count[s[right]]>1:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
            
        
        
        
#         for k in range(n+1):
#             check=Counter(s[:k])
#             if len(check)==k:
#                 ans=k
#                 continue 
                
#             for i in range(n-k):
#                 check[s[i]]-=1
#                 if check[s[i]]==0:
#                     check.pop(s[i])
#                 check[s[i+k]]+=1
#                 if len(check)==k:
#                     ans=k
                    
        return ans
                
            
        
        