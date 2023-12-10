class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        neg=[]
        pos=[]
        
        for val in nums:
            if val<0:
                neg.append(val)
            else:
                pos.append(val)
                
        ans=[]
        
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        
        return ans
        