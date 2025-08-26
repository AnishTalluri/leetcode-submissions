class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        return self.fib_helper(n, memo)

    def fib_helper(self, n, memo):
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib_helper(n-1, memo) + self.fib_helper(n-2, memo)
            return memo[n]
