class Solution:
     def findJudge(self, N, trust):
        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)
        for a, b in trust:
            in_degree[b] += 1
            out_degree[a] += 1
        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
        return -1
#法官实际上就是出度为0，入度为 N - 1的节点。
#思路就是统计所有人的入度和出度信息，将满足出度为0，入度为 N - 1的节点输出。
#用两个数组 in_degree 和 out_degree 分别记录入度和出度的信息，为了简单起见，我们初始化的数组长度为 N + 1，而不是 N。
