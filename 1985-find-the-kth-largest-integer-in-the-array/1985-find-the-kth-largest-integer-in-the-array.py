class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ans=[int(j) for j in nums]
        ans.sort(reverse=True)
        return str(ans[k-1])