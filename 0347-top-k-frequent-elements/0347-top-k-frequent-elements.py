class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        ans=[]
        cur=nums[0]
        count=0
        for i in range(len(nums)):
            if cur== nums[i]:
                count+=1
            else :
                ans.append((count,nums[i-1]))
                cur=nums[i]
                count=1
            if i==len(nums)-1:
                ans.append((count,nums[i]))
                cur=nums[i]
                count=1
        ans.sort()
        ans2=[]
        for j in range(k):
            t=ans.pop()
            ans2.append(t[1])
        return ans2
        
