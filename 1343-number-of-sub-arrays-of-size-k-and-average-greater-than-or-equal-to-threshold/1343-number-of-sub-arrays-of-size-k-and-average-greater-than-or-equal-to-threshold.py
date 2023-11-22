class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        s=sum(arr[:k])
        ans=0
        if s/k>=threshold:
            ans+=1
        for i in range(n-k):
            s-=arr[i]
            s+=arr[i+k]
            if s/k>=threshold:
                ans+=1
        # print(arr)
        return ans 