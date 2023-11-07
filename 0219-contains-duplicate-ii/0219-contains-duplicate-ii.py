class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ind={}
        n=len(nums)
        
        for i in range(n):
            val=nums[i]
            if val in ind and i-ind[val]<=k:
                    return True 
            ind[val]=i
        return False
                
                
            