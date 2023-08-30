class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        def track():
            if len(nums)==len(temp):
                    ans.append(temp[:])
                    return 
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    track()
                    temp.pop()
        track()            
        return ans   
            