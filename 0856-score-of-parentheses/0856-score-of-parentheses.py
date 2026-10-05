class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                # If we encounter an immediate "()", add 2^depth to score
                if s[i - 1] == '(':
                    score += 1 << depth
                    
        return score