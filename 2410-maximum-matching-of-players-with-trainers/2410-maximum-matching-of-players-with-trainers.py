class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j=0
        m=len(players)
        n=len(trainers)
        ans=0
        for i in range(n):
            if j==m:
                break
            if trainers[i]>=players[j]:
                j+=1
                ans+=1
        return  ans
                
        