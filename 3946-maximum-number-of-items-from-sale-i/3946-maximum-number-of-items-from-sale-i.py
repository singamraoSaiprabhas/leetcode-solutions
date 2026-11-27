from collections import Counter
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        if not items or budget <= 0:
            return 0

        # 1. Count how many free copies each distinct factor generates
        freq = Counter(f for f, _ in items)
        max_f = max(freq)
        distinct = len(freq)
        free_map = {}

        if max_f <= 200_000 and max_f <= distinct * distinct:
            for f in freq:
                total = 0
                for m in range(f, max_f + 1, f):
                    if m in freq:
                        total += freq[m]
                free_map[f] = total - 1
        else:
            factors = sorted(freq)
            for idx, f1 in enumerate(factors):
                total = freq[f1] - 1
                for f2 in factors[idx + 1:]:
                    if f2 % f1 == 0:
                        total += freq[f2]
                free_map[f1] = total

        # 2. Filter items whose first copy beats buying extra copies of min_price
        min_price = min(p for _, p in items)
        candidates = []
        for f, p in items:
            val = 1 + free_map[f]
            if p <= budget and val > p // min_price:
                candidates.append((p, val))

        max_cost = min(budget, sum(p for p, _ in candidates))
        max_val = sum(v for _, v in candidates)

        # 3. 0/1 Knapsack on whichever dimension is smaller (cost vs. value)
        if max_cost <= max_val:
            dp = [0] * (max_cost + 1)
            cur_cap = 0
            for p, v in candidates:
                cur_cap = min(max_cost, cur_cap + p)
                for w in range(cur_cap, p - 1, -1):
                    cand = dp[w - p] + v
                    if cand > dp[w]:
                        dp[w] = cand

            return max(
                dp[w] + (budget - w) // min_price
                for w in range(max_cost + 1)
            )
        else:
            INF = budget + 1
            dp = [INF] * (max_val + 1)
            dp[0] = 0
            cur_val = 0
            for p, v in candidates:
                cur_val += v
                for val in range(cur_val, v - 1, -1):
                    new_cost = dp[val - v] + p
                    if new_cost < dp[val]:
                        dp[val] = new_cost

            return max(
                val + (budget - dp[val]) // min_price
                for val in range(max_val + 1)
                if dp[val] <= budget
            )