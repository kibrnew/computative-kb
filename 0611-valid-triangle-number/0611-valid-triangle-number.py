class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        ans=0
        n=len(nums)
        
        
        for i in range(n-2):
            temp=deque()
            j=i+1
            while j<=n:
                while j<n and (len(temp)<1 or nums[j]-temp[0]<nums[i]):
                    temp.append(nums[j])
                    j+=1
                ans+=max(0,len(temp)-1)
                if len(temp)==0:
                    j+=1
                else:
                    temp.popleft()

        return ans