class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        ans=0
        while trainers and players: 
            if trainers[-1]>=players[-1]:
                ans+=1
                players.pop()
            trainers.pop()
            
        return ans
        