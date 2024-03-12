class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l=0
        r=len(nums)-1

        while l<=r:
            mid=l+(r-l)//2

            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid-1

        right=r

        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2

            if nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1

        left=l
        print(left,right)

        if left>right:
            return [-1,-1]
        return [left,right]

        # return [1,1]
        