class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        nums=sorted(arr)
        ans=set()
        for cur in range(len(nums)-2):
            pr1=cur+1
            pr2=len(nums)-1
            while pr1<pr2:
                if nums[cur]+nums[pr1]+nums[pr2]==target:
                    ans.add((nums[cur],nums[pr1],nums[pr2]))
                    pr1+=1
                    pr2-=1
                elif nums[cur]+nums[pr1]+nums[pr2]<target:
                    pr1+=1
                else:
                    pr2-=1
        c=Counter(nums)
        summ=0
        for num in ans:
            i=0
            p=1
            while i<3:
                n=num[i]
                am=num.count(n)
                p*=comb(c[n],am)
                i+=am
            summ+=p
        return summ%((10**9)+7)
                


