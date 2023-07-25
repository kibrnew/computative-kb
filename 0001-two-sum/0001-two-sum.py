class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(bool)
        ans=[]
        for i in nums:
            if d[i]:
                ans.append(nums.index(i))
                ans.append(len(nums)-nums[::-1].index(target-i)-1)
                return ans
            else:
                comp=target-i
                d[comp]=1
            
                
                
        
        