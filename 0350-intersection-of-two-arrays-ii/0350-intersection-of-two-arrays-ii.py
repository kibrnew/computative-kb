class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        def search(arr,val):
            left=0
            right=len(arr)-1
            while left<=right:
                mid=left+(right-left)//2
                if arr[mid]==val:
                    return True 
                elif arr[mid]>val:
                    right=mid-1
                else:
                    left=mid+1
            return False 
        ans=[]
        count=Counter(nums1)
        for num in nums2:
            if search(nums1,num) and count[num]>0:
                count[num]-=1
                ans.append(num)
        return ans
        