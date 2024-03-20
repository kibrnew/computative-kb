class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count=Counter()
        prefix=[None]
        maxi=-1
        for val in persons:
            count[val]+=1
            if count[val]>=count[maxi]:
                prefix.append(val)
                maxi=val
            else:
                prefix.append(maxi)

        self.times=times
        self.ans=prefix
        

    def q(self, t: int) -> int:
        ind=bisect_right(self.times,t)
        return self.ans[ind]
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)