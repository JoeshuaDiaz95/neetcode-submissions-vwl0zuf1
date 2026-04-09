class MinStack:

    def __init__(self):
        self.Minstack = []

    def push(self, val: int) -> None:
        self.Minstack.append(val)
        

    def pop(self) -> None:
        self.Minstack.pop()

    def top(self) -> int:
        return self.Minstack[-1]

    def getMin(self) -> int:
        if self.Minstack:
            currmin = self.Minstack[0]
        for value in self.Minstack:
            if value < currmin:
                currmin = value
        return currmin
            
