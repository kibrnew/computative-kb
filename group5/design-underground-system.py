class UndergroundSystem:

    def __init__(self):
        
        self.status={}
        self.journey= defaultdict(lambda :[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.status[id]=(stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        start,t_start=self.status[id]
        
        self.journey[(start,stationName)][1]+=1
        self.journey[(start,stationName)][0]+=t-t_start
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        total_time,person=self.journey[(startStation,endStation)]
        
        return total_time/person
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)