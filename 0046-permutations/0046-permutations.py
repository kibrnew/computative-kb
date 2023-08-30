class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        visited=set()
        ans=[]
        def track():
            for num in nums:
                if len(nums)==len(temp):
                    ans.append(temp[:])
                    return 
                if num not in visited:
                    temp.append(num)
                    visited.add(num)
                    track()
                    temp.pop()
                    visited.remove(num)
        track()            
        return ans   
            