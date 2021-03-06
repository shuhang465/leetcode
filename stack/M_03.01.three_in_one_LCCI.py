# 三合一。描述如何只用一个数组来实现三个栈。
# 你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
# 构造函数会传入一个stackSize参数，代表每个栈的大小。

#这个题就是说一个数组里有三个栈，比如1到5是一个栈，5到10是一个栈
#这个题的做法是让栈顶在左侧，就是顶000顶000顶000
class TripleInOne:
    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.stack = [0] * 3 * stackSize
#         dict1.fromkeys((1,2,3),'number')
#         {1: 'number', 2: 'number', 3: 'number'}
        #top用来判断是否满栈
        self.top = dict.fromkeys(range(3), 0)

    def push(self, stackNum: int, value: int) -> None:
        #如果是满栈就不能push了
        if self.top[stackNum] == self.stackSize: return
        self.stack[stackNum * self.stackSize + self.top[stackNum]] = value
        self.top[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        #如果是空的不能pop
        if not self.top[stackNum]: return -1
        val = self.stack[stackNum * self.stackSize + self.top[stackNum] - 1]
        self.top[stackNum] -= 1
        return val

    def peek(self, stackNum: int) -> int:
        if not self.top[stackNum]: return -1
        return self.stack[stackNum * self.stackSize + self.top[stackNum]-1] 

    def isEmpty(self, stackNum: int) -> bool:
        return not self.top[stackNum]


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
