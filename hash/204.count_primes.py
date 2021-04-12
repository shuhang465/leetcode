class Solution:
    def countPrimes(n):
        is_prime = [True]*(n+1)
        ans = 0
        for num in range(2,n+1):
            if is_prime[num]:
                ans+=1
                for k in range(1,n//num+1):
                    is_prime[num*k]=False
        return ans
#合数可以由若干质数相乘得到，所以质数的倍数是合数，假设所有数都是质数，然后除去倍数
        
