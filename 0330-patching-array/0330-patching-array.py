class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        maxi=0
        ans=0
        nums.append(n+1)
        for val in nums:
            if maxi>=n:
                break
            while maxi<n and maxi<val-1:
                maxi=2*maxi+1
                ans+=1
            maxi+=val
        return ans
                
        