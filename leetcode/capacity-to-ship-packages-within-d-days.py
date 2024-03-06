class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        

        def check(nums,capacity):
            ans=1
            cur=0
            for val in nums:
                if val+cur<=capacity:
                    cur+=val
                else:
                    ans+=1
                    cur=val
            return ans


        r=sum(weights)
        l=max(weights)

        while l<=r:
            mid=l+(r-l)//2
            if check(weights,mid)<=days:
                r=mid-1
            else:
                l=mid+1

        return l






        