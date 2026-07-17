class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        cnt = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for multiple in range(g, max_val + 1, g):
                cnt[g] += freq[multiple]
                
        gcd_count = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            total_pairs = (cnt[g] * (cnt[g] - 1)) // 2
           
            sub_pairs = 0
            for multiple in range(2 * g, max_val + 1, g):
                sub_pairs += gcd_count[multiple]
            gcd_count[g] = total_pairs - sub_pairs
            
        prefix_sums = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            prefix_sums[g] = prefix_sums[g - 1] + gcd_count[g]
        ans = []
        for q in queries:
            g = bisect.bisect_right(prefix_sums, q)
            ans.append(g)
            
        return ans