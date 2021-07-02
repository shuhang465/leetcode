# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return []
        res = []
        #最原始的做法就是深度优先遍历，root就是‘’,然后对左面的（和右面的）分别遍历，终止条件是len(paths)=n*2
        #但是可以剪枝，所以加入left和right两个计数，如果right>left就错，left>n,right>n就错误
        def dfs(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return 
            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res
