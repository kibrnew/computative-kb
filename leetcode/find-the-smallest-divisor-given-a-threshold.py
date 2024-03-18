class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        nums.sort()

        def calc(k):
            ans=0
            for val in nums:
                ans+=(val+k-1)//k

            return ans
        
        l=1
        r=max(nums)

        while l<=r:
            mid=(l+r)//2
            if calc(mid)<=threshold:
                r=mid-1
            else:
                l=mid+1

        # print(nums[l])

        return l