class MinStack:

    def __init__(self):
        self.stack=[]
        self.temp=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack :
            return False 
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack :
            return False 
        return min(self.stack)
        """
        minimum=self.pop()
        self.temp.append(minimum)
        for i in range(len(self.stack)):
            cur=self.pop()
            self.temp.append(cur)
            if minimum>cur:
                minimum=cur
        for j in range(len(self.temp)):
            t=self.temp.pop()
            self.stack.append(t)
        return minimum """
            
            
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()