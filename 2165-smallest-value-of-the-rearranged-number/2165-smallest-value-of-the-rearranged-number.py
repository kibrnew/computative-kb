class Solution:
    def smallestNumber(self, num: int) -> int:
        
        def sorter(val):
            
            count=Counter(list(str(val)))
            ans=[]
            
            for i in range(10):
                ans.extend([str(i)]*count[str(i)])
                
            return ans
        
        if num<=0:
            num*=-1
            return -1*int("".join(sorter(num)[::-1]))
        else:
            new=sorter(num)
            ind=bisect_right(new,"0")
            new[0],new[ind]=new[ind],new[0]
            return int("".join(new))
            
            
            