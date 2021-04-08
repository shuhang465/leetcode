class MinStack:

    def __init__(self):
        self.A = []
        self.B = []

    #B用于存放最小值，如果有比更小的值则入栈
    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)
    #如果A出栈正好等于B的栈顶，那么最小值没有了，B也要出栈
    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
