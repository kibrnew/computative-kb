class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        ans=0
        count=Counter()
        c=0
        for val in arr:
            count[c]+=1
            if val%2==1:
                c^=1
            ans+=count[c^1]
            
        return ans%(10**9 + 7)
                
        