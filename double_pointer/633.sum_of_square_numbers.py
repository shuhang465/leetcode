class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j=0,int(c**0.5)
        while i<=j:
            if i*i+j*j==c:
                return True
            elif i*i+j*j>c:
                j-=1
            elif i*i+j*j<c:
                i+=1
        return False
