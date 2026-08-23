class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_left, sum_right = 0, 0
        q_left, q_right = 0, 0
        
        # Parse the left half
        for i in range(half):
            if num[i] == '?':
                q_left += 1
            else:
                sum_left += int(num[i])
                
        # Parse the right half
        for i in range(half, n):
            if num[i] == '?':
                q_right += 1
            else:
                sum_right += int(num[i])
                
        # Condition 1: Total question marks are odd (Alice gets the last move)
        if (q_left + q_right) % 2 != 0:
            return True
            
        # Condition 2: Total question marks are even (Bob gets the last move)
        # Check if the initial sum difference can be exactly offset by the '?' difference
        if 2 * (sum_left - sum_right) == 9 * (q_right - q_left):
            return False
            
        return True