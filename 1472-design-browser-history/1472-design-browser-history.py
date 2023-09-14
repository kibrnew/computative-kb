class BrowserHistory:
    def __init__(self, homepage: str):
        self.history=[homepage]
        self.indx=0

    def visit(self, url: str) -> None:
        self.indx+=1
        self.history=self.history[:self.indx]
        self.history.append(url)
        return url
    def back(self, steps: int) -> str:
        self.indx-=steps
        if self.indx>0:
            return self.history[self.indx]
        self.indx=0
        return self.history[self.indx]
    def forward(self, steps: int) -> str:
        self.indx+=steps
        if self.indx<len(self.history):
            return self.history[self.indx]
        self.indx=len(self.history)-1
        return self.history[self.indx]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)