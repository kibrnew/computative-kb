class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
#         ans=1
#         for w in range(2,n+1):
#             l=w*nums[w-1]
#             s=sum(nums[:w])

#             if l-s<=k:
#                 ans=w
#                 continue
                
#             for i in range(n-w):
#                 l=w*nums[w+i]
#                 s-=nums[i]
#                 s+=nums[w+i]
                
#                 if l-s<=k:
#                     ans=w
#                     break
#         return ans
    
        s=nums[0]
        l=0
        ans=1
        for r in range(1,n):
            s+=nums[r]
            
            while k<nums[r]*(r-l+1)-s:
                s-=nums[l]
                l+=1
                
            ans=max(ans,r-l+1)
        return ans
    
    
                    
                
        
       