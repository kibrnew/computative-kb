class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        
        def calc(nums):
            count={}
            ans=[]
            for i,val in enumerate(nums):
                if val in count:
                    s,c=count[val]
                    ans.append(c*i-s)
                    count[val]=(s+i,c+1)
                else:
                    count[val]=(i,1)
                    ans.append(0)
            return ans
        
        left=calc(nums)
        right=calc(nums[::-1])
        
        res=[l+r for l,r in zip(left,right[::-1])]
        
        return res
        
        

                
            
                
            
            