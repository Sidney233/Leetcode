from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hight = len(cost)
        dp = [0] * (hight + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, hight + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[hight]
