class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        ans=[]
        deck.sort()
        n=len(deck)
        new=[]
        off=0
        while n>2:
            cur=(n+1)//2
            new.append(deck[off:off+cur])
            off+=cur
            n-=cur

        if off<len(deck):
            new.append(deck[off:])

        # print(new)
        new=new[::-1]
        prev=deque(new[0])

        for nums in new[1:]:
            r=[]
            if len(nums)>len(prev):
                q=prev.pop()
                prev.appendleft(q)

            for val in nums:
                r.append(val)

                if prev:
                    r.append(prev.popleft())

            prev=deque(r)


        return prev