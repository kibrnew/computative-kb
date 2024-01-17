class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n=len(arr)
        ans=0
        for i in range(n):
            val=(n-i+1)//2
            t=val+val*i
            if i%2!=n%2:
                t-=(i+1)//2
            ans+=t*(arr[i])
        return ans
            
            