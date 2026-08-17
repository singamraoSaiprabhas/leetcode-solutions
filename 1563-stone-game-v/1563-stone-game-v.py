from typing import List
from functools import cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dfs(left: int, right: int) -> int:
            # Only one stone remains
            if left >= right:
                return 0

            ans = 0

            # Sum of the entire interval
            right_sum = prefix[right + 1] - prefix[left]
            left_sum = 0

            for k in range(left, right):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    # Alice keeps the left part.
                    #
                    # Maximum possible future score from this
                    # part is less than left_sum, so if
                    # 2 * left_sum <= ans, this split cannot help.
                    if left_sum * 2 <= ans:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(left, k)
                    )

                elif left_sum > right_sum:
                    # Alice keeps the right part.
                    #
                    # As k increases, right_sum only decreases.
                    # Once 2 * right_sum <= ans, later splits
                    # cannot improve the answer.
                    if right_sum * 2 <= ans:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, right)
                    )

                else:
                    # Equal sums: Alice can choose either side.
                    ans = max(
                        ans,
                        left_sum + dfs(left, k),
                        right_sum + dfs(k + 1, right)
                    )

            return ans

        return dfs(0, n - 1)