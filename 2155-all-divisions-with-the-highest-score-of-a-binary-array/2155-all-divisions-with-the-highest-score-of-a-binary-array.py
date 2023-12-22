class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        one=nums.count(1)
        n=len(nums)
        count={}
        count[-1]=one
        zero=0
        
        for i in range(n):
            if nums[i]==0:
                zero+=1
            else:
                one-=1
            count[i]=zero+one
        
        maxi=max(count.values())
        ans=[]
        for key,val in count.items():
            if val==maxi:
                ans.append(key+1)
        return ans
            
            
        