class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radient=deque()
        dire=deque()
        n=len(senate)
        for index,senator in enumerate(senate):
            if senator=="R":
                radient.append(index)
            else:
                dire.append(index)
        while radient and dire:
            rindx=radient.popleft()
            dindx=dire.popleft()
            
            if rindx<dindx:
                radient.append(rindx+n)
            else :
                dire.append(dindx+n)
        if radient:
            return "Radiant"
        else :
            return "Dire"