class Solution(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()            
            for i in range(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])

#倒着来
