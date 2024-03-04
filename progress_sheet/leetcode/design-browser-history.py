class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=homepage
        self.stack=[homepage]
        self.bac=[]
    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.bac=[]
    def back(self, steps: int) -> str:
        for _ in range(steps):
                if len(self.stack)>1:
                    self.bac.append(self.stack.pop())
        return self.stack[-1]
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.bac:
                self.stack.append(self.bac.pop())
        return self.stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)