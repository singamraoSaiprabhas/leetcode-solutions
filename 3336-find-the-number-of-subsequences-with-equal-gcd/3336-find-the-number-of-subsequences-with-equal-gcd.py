class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def dp(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 > 0 else 0
            ways = dp(i + 1, g1, g2)
            ways = (ways + dp(i + 1, math.gcd(g1, nums[i]), g2)) % MOD
            ways = (ways + dp(i + 1, g1, math.gcd(g2, nums[i]))) % MOD
            return ways
        return dp(0, 0, 0)