class ATM:

    def __init__(self):
        
        self.notes=[0,0,0,0,0]
        self.ind=[20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        
        for i in range(len(banknotesCount)):
            val=banknotesCount[i]
            self.notes[i]+=val
        
        

    def withdraw(self, amount: int) -> List[int]:
        
        ans=[]
        n=len(self.ind)
        for i in range(n-1,-1,-1):
            
            val=self.ind[i]
            
            number=amount//val
            
            if self.notes[i]>=number:
                self.notes[i]-=number
                amount-=val*number
                ans.append(number)
            
            else:
                amount-=self.notes[i]*val
                
                ans.append(self.notes[i])
                self.notes[i]=0
                
        ans=ans[::-1]
        
        if not amount:
            return ans
        else:
            for i in range(len(ans)):
                self.notes[i]+=ans[i]
            return [-1]
            
            
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)