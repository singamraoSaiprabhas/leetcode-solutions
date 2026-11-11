class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def get_cost(x: int) -> int:
            return (x * costBoth) + (max(0, need1 - x) * cost1) + (max(0, need2 - x) * cost2)
        
        return min(get_cost(0), get_cost(need1), get_cost(need2))