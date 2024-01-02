class RandomizedSet:

    def __init__(self):
        self.arr=[]
        self.ind={}
        
     
    def insert(self, val: int) -> bool:
        if val in self.ind:
            return False
        self.arr.append(val)
        self.ind[val]=len(self.arr)-1
        return True

    
    def remove(self, val: int) -> bool:
        if val in self.ind:
            i=self.ind[val]
            self.arr[i],self.arr[-1]=self.arr[-1],self.arr[i]
            self.ind[self.arr[i]]=i
            self.arr.pop()
            self.ind.pop(val)
            return True
        return False
    
    def getRandom(self) -> int:
        i=randint(0,len(self.arr)-1)
        return self.arr[i]
        
       

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()