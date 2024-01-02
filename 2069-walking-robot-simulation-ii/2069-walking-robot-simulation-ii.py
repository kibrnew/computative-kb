class Robot:

    def __init__(self, width: int, height: int):
        
        self.xf=width-1
        self.yf=height-1
        self.direction=["East","North","West","South"]
        self.curr=0
        

    def step(self, num: int) -> None:
        self.curr+=num
        

    def getPos(self) -> List[int]:
        t=self.xf+self.yf
        ans=self.curr//t
        rem=self.curr%t
        if ans%2:
            if rem>self.xf:
                return [0,self.yf-(rem-self.xf)]
            else:
                return [self.xf-rem,self.yf]
        else:
            if rem>self.xf:
                return [self.xf,rem-self.xf]
            else:
                return [rem,0]
            

    def getDir(self) -> str:
        flag=False
        if self.curr>0:
            self.curr-=1
            flag=True
            
        t=self.xf+self.yf
        ans=self.curr//t
        rem=self.curr%t
        i=(ans%2)*2
        
        if rem>=self.xf:
            i+=1
        # print(i,self.curr,ans,rem)
        # print(self.xf,self.yf)
        if flag:
            self.curr+=1 
        return self.direction[i]
        
        
        
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()