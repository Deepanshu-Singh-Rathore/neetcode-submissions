class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = list()
    def push(self, val: int):
        self.stack.append(val)
        if len(self.minstack) != 0:
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)
        
    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]
