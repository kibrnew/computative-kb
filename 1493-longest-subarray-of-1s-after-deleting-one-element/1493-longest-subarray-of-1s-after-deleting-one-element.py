class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        ans=0
        prev=0
        flag=True
        count=0
        p=0
        for i in nums:
            if i==1:
                count+=1
            else:
                if p==0:
                    prev=0
                    flag=False
                    count=0
                elif flag:
                    ans=max(ans,prev+count)
                    prev=count
                    count=0
                else:
                    ans=max(count,ans)
                    prev=count
                    count=0
                    flag=True
            p=i
        ans=max(count,ans)
        if flag:
            ans=max(ans,prev+count)
            flag=False
            prev=0
        return ans
                    
            