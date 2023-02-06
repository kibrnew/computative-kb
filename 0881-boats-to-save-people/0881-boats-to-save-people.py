class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        pointer1=0
        pointer2=len(people)-1
        while pointer1<pointer2:
            summ=people[pointer1]+people[pointer2]
            if summ<=limit:
                n=n-1
                pointer1=pointer1+1
                pointer2=pointer2-1
            else:
                pointer2=pointer2-1
        return n
                