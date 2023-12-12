class OrderedStream:

    def __init__(self, n: int):
        self.id=[None]*n
        self.start=0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        
        i=idKey-1
        
        self.id[i]="".join(value)
        n=len(self.id)
        prev=self.id
        ans=[]
        
        while self.start==i and i<n :
            
            ans.append(self.id[i])
            i+=1
            self.start+=1
            if i<n and not self.id[i]:
                break
                
        return ans
                
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)