class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        pr1=0
        pr2=len(nums)-1
        while pr1<=pr2:
            ans.append(nums[pr1])
            if pr1==pr2:
                break
            pr1+=1
            ans.append(nums[pr2])
            pr2-=1
        return ans
            
            
        