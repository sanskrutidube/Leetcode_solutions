class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  

    def push(self, val: int) -> None:
        self.stack.append(val)  
        if not self.min_stack or val <= self.min_stack[-1]:  
            self.min_stack.append(val)  

    def pop(self) -> None:
        if self.stack:  
            if self.stack[-1] == self.min_stack[-1]:  
                self.min_stack.pop()  
            self.stack.pop()  

    def top(self) -> int:
        if self.stack:  
            return self.stack[-1]  

    def getMin(self) -> int:
        if self.min_stack: 
            return self.min_stack[-1]  
   -----------------------------------------------------------
  
  class MinStack:
    def __init__(self):
        self.A = []
        self.M = []
    def push(self, x):
        self.A.append(x)
        self.M.append( x if not self.M else min(x, self.M[-1]) )
    def pop(self):
        self.A.pop()
        self.M.pop()
    def top(self):
        return self.A[-1]
    def getMin(self):
        return self.M[-1]
