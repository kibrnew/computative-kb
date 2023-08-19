class Solution:
    def largestInteger(self, num: int) -> int:
        nums=[int(i) for i in list(str(num))]
        odd=[]
        even=[]
        heapify(odd)
        heapify(even)
        for i in nums:
            if i%2==0:
                heappush(even,-i)
            else:
                heappush(odd,-i)
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=-heappop(even)
            else:
                nums[i]=-heappop(odd)
        print(nums)
        k=int("".join([str(i) for i in nums]))
        return k
                
        