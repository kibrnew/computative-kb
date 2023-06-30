class Solution:
    def minOperations(self, logs: List[str]) -> int:
        start=0
        for i in logs:
            if i=="../":
                if start==0:
                    continue
                else:
                    start-=1
            elif i=="./":
                continue 
            else :
                start+=1
        return start
        