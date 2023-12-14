class FrequencyTracker:

    def __init__(self):
        
        self.tracker=defaultdict(int)
        self.fr=defaultdict(int)
        

    def add(self, number: int) -> None:
        
        prev=self.tracker[number]
        self.tracker[number]+=1
        self.fr[prev]-=1
        self.fr[prev+1]+=1
        
        

    def deleteOne(self, number: int) -> None:
        
        if self.tracker[number]>0:
            prev=self.tracker[number]
            self.tracker[number]-=1
            self.fr[prev]-=1
            self.fr[prev-1]+=1
            
        

    def hasFrequency(self, frequency: int) -> bool:
        
        return self.fr[frequency]!=0
            
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)