class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        max_diff = 100_000
        count = [0] * (max_diff + 1)
        
        # Populate frequency of absolute differences
        for a, b in zip(nums1, nums2):
            count[abs(a - b)] += 1
            
        # Greedily reduce largest differences
        for v in range(max_diff, 0, -1):
            if count[v] == 0:
                continue
            
            if k >= count[v]:
                k -= count[v]
                count[v - 1] += count[v]
                count[v] = 0
            else:
                count[v - 1] += k
                count[v] -= k
                k = 0
                break
                
        # Compute the final sum of squares
        return sum(v * v * c for v, c in enumerate(count))