class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour<len(dist)-0.99:
            return -1
        start=1
        end=ceil(max(dist)/hour)*len(dist)
        if len(dist)==ceil(hour):
            z=(hour-int(hour))
            if z==0:
               z=1
            k=ceil(dist[-1]/z)
            end=max(end,k)
        def check(arr,h):
            ans=0
            for i in arr[:-1]:
                ans+=ceil(i/h)
            ans+=arr[-1]/h
            return ans<=hour
        while start<=end:
            mid=start+(end-start)//2
            flag=check(dist,mid)
            if flag:
                end=mid-1
            else:
                start=mid+1
        if check(dist,mid):
            return mid
        return mid+1

        