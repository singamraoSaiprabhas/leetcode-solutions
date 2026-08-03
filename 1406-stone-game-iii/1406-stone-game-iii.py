class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0, 0, 0] 
        for i in range(n - 1, -1, -1):
            curr_max = float('-inf')
            stones_taken = 0
            for k in range(3):
                if i + k < n:
                    stones_taken += stoneValue[i + k]
                    curr_max = max(curr_max, stones_taken - dp[k])
            dp[2] = dp[1]
            dp[1] = dp[0]
            dp[0] = curr_max
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"