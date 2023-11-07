class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ind={}
        
        for i,val in enumerate(nums):
            if val in ind and i-ind[val]<=k:
                    return True 
            ind[val]=i
        return False
                
                
            