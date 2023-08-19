class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        num=nums[:k]
        heapify(num)
        self.nums=num
        self.k=k
    def add(self, val: int) -> int:
        ans=-float("inf")
        if len(self.nums)==self.k:
            ans=heappop(self.nums)
        heappush(self.nums,max(val,ans))
        temp=heappop(self.nums)
        heappush(self.nums,temp)
        return temp
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)