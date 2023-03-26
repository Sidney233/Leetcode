class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp = [0] * (n + 1)
            dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]


if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print(sol.fib(n))
