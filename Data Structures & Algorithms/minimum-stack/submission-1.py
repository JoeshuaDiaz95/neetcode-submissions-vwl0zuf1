class MinStack:

    def __init__(self):
        self.Minstack = []
        self.Minstackhelper = []
    def push(self, val: int) -> None:
        self.Minstack.append(val)

        if not self.Minstackhelper or val < self.Minstackhelper[-1]:
            self.Minstackhelper.append(val)
        else:
            self.Minstackhelper.append(self.Minstackhelper[-1])    
        

    def pop(self) -> None:
        self.Minstack.pop()
        self.Minstackhelper.pop()
    def top(self) -> int:
        return self.Minstack[-1]

    def getMin(self) -> int:
        return self.Minstackhelper[-1]
            
