class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, val: int) -> None:
        self.A.append(val)
        if not self.B or self.B[-1] >= val:
            self.B.append(val)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.B[-1]
