class MyQueue:

    def __init__(self):
        self.a=[]
        self.b=[]
        

    def push(self, x: int) -> None:
        self.a.append(x) 
    def pop(self) -> int:
        if not self.a:
            return False 
        while self.a :
            tempa=self.a.pop()
            self.b.append(tempa)
        ans=self.b.pop()
        while self.b:
            tempb=self.b.pop()
            self.a.append(tempb)
        return ans 

    def peek(self) -> int:
        if not self.a:
            return False 
        while self.a :
            tempa=self.a.pop()
            self.b.append(tempa)
        ans=self.b[-1]
        while self.b:
            tempb=self.b.pop()
            self.a.append(tempb)
        return ans
        
        

    def empty(self) -> bool:
        if  self.a:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()