class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <3:
            return 0
        def sieve(n):
            "Return all primes <= n."
            np1 = n + 1
            s = list(range(np1)) # leave off `list()` in Python 2
            s[1] = 0
            sqrtn = int(round(n**0.5))
            for i in xrange(2, sqrtn + 1): # use `xrange()` in Python 2
                if s[i]:
                    # next line:  use `xrange()` in Python 2
                    s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
            return filter(None, s)
        return len(list(sieve(n-1)))
#code from: http://stackoverflow.com/questions/19345627/python-prime-numbers-sieve-of-eratosthenes



if __name__ == '__main__':
    A = Solution()
    print A.countPrimes(100)