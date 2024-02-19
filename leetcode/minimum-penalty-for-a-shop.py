class Solution:
    def bestClosingTime(self, customers: str) -> int:
        one=customers.count("Y")
        zero=0
        ans=0
        res=one
        for i,val in enumerate(customers):
            if val=="N":
                zero+=1
            else:
                one-=1
            if one+zero<res:
                res=one+zero
                ans=i+1
        return ans
                