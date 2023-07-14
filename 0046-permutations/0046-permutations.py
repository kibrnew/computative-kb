class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(cur):
            if len(cur)==len(nums):
                ans.append(cur[:])
                return 
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    perm(cur)
                    cur.pop()
        ans=[]
        perm([])
        return ans
        