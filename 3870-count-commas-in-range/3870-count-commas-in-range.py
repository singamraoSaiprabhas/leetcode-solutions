class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        while n >= threshold:
            # Add 1 comma for every number from 'threshold' up to 'n'
            total_commas += (n - threshold + 1)
            # Move to the next comma boundary (e.g., from 1,000 to 1,000,000)
            threshold *= 1000
            
        return total_commas