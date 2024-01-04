class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        left=0
        right=len(people)-1
        ans=0
        people.sort()
        while left<=right:
            if people[left]+people[right]>limit:
                ans+=1
            else:
                ans+=1
                left+=1
            right-=1
        return ans
        
        
        
                