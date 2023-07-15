class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        def track():
            for num in nums:
                if len(nums)==len(temp):
                    ans.append(temp[:])
                    return 
                if num not in temp:
                    temp.append(num)
                    track()
                    temp.pop()
        track()
        return ans   
            