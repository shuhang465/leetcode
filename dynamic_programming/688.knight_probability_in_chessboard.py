class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K+1)]  # 初始化三维数组

        dp[0][r][c] = 1  # 走0步，在r，c位置的概率为1（初始条件）
        directions = [[1,2], [1, -2], [-2, 1], [-2, -1], [2, 1], 
        [2, -1], [-1,2], [-1, -2]]  # 八个方向
        for k in range(K+1):  # 对于每一步
            for i in range(N):
                for j in range(N):  # 遍历NxN个格子
                    for x, y in directions:  # 对每个格子都有8个方向可以走，循环每个方向
                        new_x, new_y = i+x, j+y
                        if 0<=new_x<N and 0<=new_y<N:  # 如果按照当前方向走完还在格子里，就作为当前步的结果，如果在格子外，就不考虑
                            dp[k][i][j] += dp[k-1][new_x][new_y] * 0.125  # 对于在格子里的情况，走到当前格子的概率都是1/8

        
        return sum(sum(i) for i in dp[-1])  # 统计一下最后一步中，每个格子的概率
