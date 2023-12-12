class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
       
        ans=[]
        s=sum(filter(lambda x:x%2==0,nums))
        res=0
        
        for val,i in queries:
            
            res=nums[i]+val
            
            if nums[i]%2==0:
                
                if res%2==0:
                    s+=val
                else:
                    s-=nums[i]
                    
            elif res%2==0:
                s+=res

            nums[i]=res
            
            ans.append(s)
         
    
        return ans
        
        # return nums