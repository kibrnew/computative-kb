class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for cur in range(len(nums)-2):
            pr1=cur+1
            pr2=len(nums)-1
            while pr1<pr2:
                if nums[cur]+nums[pr1]+nums[pr2]==0:
                    ans.add((nums[cur],nums[pr1],nums[pr2]))
                    pr1+=1
                    pr2-=1
                elif nums[cur]+nums[pr1]+nums[pr2]<0:
                    pr1+=1
                else:
                    pr2-=1
        final =[list(i) for i in ans]
        return final
                    
                
                    