class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count set bits at each bit position (up to 30 bits for nums[i] <= 10^9)
        bit_counts = [0] * 31
        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b] += 1
                    
        total_sum = 0
        
        # Construct the top k largest numbers greedily
        for _ in range(k):
            val = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            total_sum = (total_sum + val * val) % MOD
            
        return total_sum