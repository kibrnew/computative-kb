class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        diff=[]
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        prefix=[0]*(len(diff)+1)
        for i in range(len(diff)):
            prefix[i+1]=prefix[i]+diff[i]
        prefix.pop(0)
        n=len(diff)
        ind=(n-1-prefix[::-1].index(min(prefix))+1)%len(diff)
        new=diff[ind:]+diff[:ind]
        # print(ind)
        # print(diff)
        # print(new)
        # print(prefix)
        # print(len(diff))
        summ=0
        zf=0
        for i in new:
            summ+=i
            if summ<0:
                return -1
        return ind
            

