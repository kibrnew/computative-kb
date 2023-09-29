class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
    
        price.sort()
        n=len(price)
        
        l,r,ans=0,price[-1],price[-1]
        
        while l<=r:
            mid=l+(r-l)//2
            count,last=1,price[0]
            
            for i in range(1,n):
                if price[i]-last>=mid:
                    count+=1
                    last=price[i]
            if count>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans 
        