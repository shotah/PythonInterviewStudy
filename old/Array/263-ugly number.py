class Solution:
    def primes(self, n: int) -> list:
        """ Returns  a list of primes < n """
        sieve = [True] * n
        test_prime_range = [*range(3,int(n**0.5)+1,2)]
        for i in test_prime_range:
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        print(sieve)
        return [1, 2] + [i for i in range(3,n,2) if sieve[i]]

    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        if n < 1: return False
        for prime in self.primes(n):
            if n % prime == 0 and prime > 5:
                return False
        return True


n = 8
# n= 6
n = 14
n= 7
print([*range(3,int(n**0.5)+1,2)])

print(
  Solution().isUgly(n)
)
