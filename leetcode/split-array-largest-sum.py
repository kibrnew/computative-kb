class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:


        def calc(t):
            ans=1
            temp=0
            for val in nums:
                if val+temp<=t:
                    temp+=val
                else:
                    ans+=1
                    temp=val

            return ans
                

        l=0
        r=sum(nums)
        while l<=r:
            mid=(l+r)//2
            if calc(mid)<=k:
                r=mid-1
            else:
                l=mid+1

        nums.append(l)

        return max(nums)
                


        