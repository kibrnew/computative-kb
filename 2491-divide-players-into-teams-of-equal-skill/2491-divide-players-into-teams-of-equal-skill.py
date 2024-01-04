class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        n=len(skill)
        left=skill[:n//2]
        right=skill[n//2:][::-1]
        
        target=left[0]+right[0]
        ans=left[0]*right[0]
        for a,b in zip(left[1:],right[1:]):
            if a+b==target:
                ans+=a*b
            else:
                return -1
        return ans
        