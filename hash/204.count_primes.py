class Solution:
    def countPrimes(self, n: int) -> int:
        isprime = [True] * n
        rt = 0
        for i in range(2, n):
            if isprime[i]:
                rt += 1
                j = i+i
                while j < n:
                    isprime[j]=False
                    j += i
        return rt

#合数可以由若干质数相乘得到，所以质数的倍数是合数，假设所有数都是质数，然后除去倍数
        
