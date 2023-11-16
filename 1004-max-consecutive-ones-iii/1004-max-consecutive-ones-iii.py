class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        pr1=0
        n=len(nums)
        maxi=0
        ans=0
        for i,val in enumerate(nums):
            count[val]+=1
            maxi=max(maxi,count[1])
            if i-pr1>=k+maxi:
                count[nums[pr1]]-=1
                pr1+=1  
            ans=max(ans,i-pr1+1)
        return ans 