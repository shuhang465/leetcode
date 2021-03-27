#定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
class MinStack:
#A:9 10 7 3 5
#B:9 7 3
#push:若栈B为空或者该元素小于B的栈顶元素，则将该元素压入栈中
#pop:若栈B顶的元素和栈A顶的元素一样，则该元素从B中出栈
#top:返回A的栈顶
#min:返回B的栈顶
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

