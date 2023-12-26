class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        mini=[]
        eq=[]
        maxi=[]
        
        for val in nums:
            if val==pivot:
                eq.append(val)
            elif val<pivot:
                mini.append(val)
            else: 
                maxi.append(val)
        return mini+eq+maxi
        
        