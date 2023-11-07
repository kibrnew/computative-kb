class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ind=defaultdict(lambda :-1)
        
        for i,val in enumerate(nums):
            if ind[val]!=-1:
                if i-ind[val]<=k:
                    return True 
            ind[val]=i
        return False
                
                
            