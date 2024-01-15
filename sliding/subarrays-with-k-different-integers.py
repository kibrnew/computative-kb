class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atmostk(k):
            ans=0
            l=0
            n=len(nums)
            count=Counter()
            for r in range(n):
                count[nums[r]]+=1
                while len(count)>k:
                    count[nums[l]]-=1
                    if count[nums[l]]==0:
                        count.pop(nums[l])
                    l+=1
                ans+=r-l+1
            return ans
        return atmostk(k)-atmostk(k-1)
                    
                

        
#         count = Counter()
#         l=r=0
#         ans=0
#         for val in nums:
#             count[val]+=1
#             if len(count)>k:
#                 count.pop(nums[r])
#                 r+=1
#                 l=r
            
#             if len(count)==k:
#                 while count[nums[r]]>1:
#                     count[nums[r]]-=1
#                     r+=1
#                 ans+=r-l+1
        # return ans
            
        
        
                
       
        