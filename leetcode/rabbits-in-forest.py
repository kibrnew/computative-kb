class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        
        count={}
        for val in answers:
            if val==0:
                continue
            if val in count:
                count[val]-=1
                if count[val]==0:
                    count.pop(val)
            else:
                count[val]=val
                
        ans=len(answers)
        for val in count.values():
            ans+=val
        return ans
        