# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        def remove(stack, x):
            for i in x:
                if stack and i == '#':
                    stack.pop()
                if i!= '#':
                    stack.append(i)
            return stack
        remove(stack1, s)
        remove(stack2, t)
        return stack1 == stack2
