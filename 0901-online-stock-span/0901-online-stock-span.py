class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.count={}

    def next(self, price: int) -> int:
        ans=1
        temp=[]
        while self.stack and self.stack[-1]<=price:
            now=self.stack.pop()
            ans+=self.count[now]
        self.count[price]=ans
        self.stack.append(price)
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)