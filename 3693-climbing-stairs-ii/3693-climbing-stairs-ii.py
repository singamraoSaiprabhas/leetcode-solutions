class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        prev3 = float('inf')
        prev2 = float('inf')
        prev1 = 0
        
        for i in range(1, n + 1):
            # The cost to jump to step i is costs[i-1] (since costs is 0-indexed in Python) 
            # plus the minimum jump penalty from i-1, i-2, or i-3
            current_cost = costs[i - 1] + min(
                prev1 + 1,  # Jump of 1: (1)^2 = 1
                prev2 + 4,  # Jump of 2: (2)^2 = 4
                prev3 + 9   # Jump of 3: (3)^2 = 9
            )
            
            # Shift the variables forward for the next iteration
            prev3, prev2, prev1 = prev2, prev1, current_cost
            
        return prev1