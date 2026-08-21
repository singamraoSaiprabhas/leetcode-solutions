class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Precompute the LCM for all possible subsets using bit manipulation
        subsets = []
        # Iterate from 1 to (2^n - 1)
        for i in range(1, 1 << n): 
            current_lcm = 1
            set_bits = 0
            
            # Check which coins are included in the current subset 'i'
            for j in range(n):
                if i & (1 << j):
                    current_lcm = math.lcm(current_lcm, coins[j])
                    set_bits += 1
            
            # PIE: Odd number of elements -> add (1), Even -> subtract (-1)
            sign = 1 if set_bits % 2 != 0 else -1
            subsets.append((current_lcm, sign))
            
        # Binary Search limits
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Count valid amounts <= mid using our precomputed subsets
            count = 0
            for lcm_val, sign in subsets:
                count += sign * (mid // lcm_val)
            
            # Adjust binary search window
            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans