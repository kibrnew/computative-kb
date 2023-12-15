class Bitset:

    def __init__(self, size: int):
        
        self.bit=[0]*size
        self.countt=0
        self.flipp=False
        

    def fix(self, idx: int) -> None:
        
        if not self.flipp:
            
            if self.bit[idx]==0:
                self.countt+=1
                self.bit[idx]=1
            
        else:
            
            if self.bit[idx]==1:
                self.countt+=1
                self.bit[idx]=0
        
        

    def unfix(self, idx: int) -> None:
        
        if not self.flipp:
            
            if self.bit[idx]==1:
                self.countt-=1
                self.bit[idx]=0
        
            
        else:
            
            if self.bit[idx]==0:
                self.countt-=1
                self.bit[idx]=1
            

    def flip(self) -> None:
        
        self.flipp=not(self.flipp)
        self.countt=len(self.bit)-self.countt

    def all(self) -> bool:
        
        return len(self.bit)==self.countt
            

    def one(self) -> bool:
        
         return self.countt>0
        

    def count(self) -> int:
        
        return self.countt
        

    def toString(self) -> str:
        
        ans=self.bit[::]
        
        if self.flipp:
            for i in range(len(ans)):
                ans[i]^=1
            
        return "".join([str(val) for val in ans])
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()