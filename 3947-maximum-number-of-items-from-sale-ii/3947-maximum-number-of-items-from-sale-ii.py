class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        min_price = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        # Count occurrences of every factor across all items
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        # Only items cheaper than 2 * min_price are worth buying for their free-copy bonus
        candidates = [
            (price, factor) for factor, price in items if price < 2 * min_price
        ]
        candidates.sort()

        # Count valid freebies (multiples of factor, excluding the item itself)
        mult_count = {}
        for _, factor in candidates:
            if factor not in mult_count:
                mult_count[factor] = sum(freq[factor::factor]) - 1

        total_items = 0
        for price, factor in candidates:
            if budget < price:
                break
            free_limit = mult_count[factor]
            if free_limit > 0:
                buy = min(free_limit, budget // price)
                total_items += 2 * buy
                budget -= buy * price

        # Spend remaining budget on single copies of the cheapest item
        total_items += budget // min_price
        return total_items