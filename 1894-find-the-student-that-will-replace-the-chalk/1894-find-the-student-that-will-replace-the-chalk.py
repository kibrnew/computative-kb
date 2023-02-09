class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = 0
        for i in range(len(chalk)):
            tot+=chalk[i]
            chalk[i]= tot
        n=k%chalk[-1]
        for j in range(len(chalk)):
            if n<chalk[j]:
                return j
            
            
            
        