class Solution:
    def smallestNumber(self, num: int) -> int:

        if num>0:
            ans=sorted(list(str(num)))
            if ans[0]=="0":
                ind=bisect_right(ans,"0")
                ans[0],ans[ind]=ans[ind],ans[0]
            return int("".join(ans))
        else:
            num=num*-1
            ans=sorted(list(str(num)),reverse=True)
            return -1*int("".join(ans))
        