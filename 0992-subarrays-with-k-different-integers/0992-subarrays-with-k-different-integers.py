class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def check(nums,k):
            n=len(nums)
            ans=0
            l=0
            count=Counter()

            for r in range(n):
                count[nums[r]]+=1
                while len(count)>k:
                    count[nums[l]]-=1
                    if count[nums[l]]==0:
                        count.pop(nums[l])
                    l+=1 
                ans+=(r-l+1)
            return ans 
                
        return check(nums,k)-check(nums,k-1)
                
        