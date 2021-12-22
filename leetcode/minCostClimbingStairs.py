class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        cost.append(0)
        for idx in range(len(cost) - 2):
            cost[idx + 2] += min(cost[idx + 1], cost[idx])
        return cost[-1]