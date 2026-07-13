class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequence = "123456789"
        result = []
        min_len = len(str(low))
        max_len = len(str(high))
        
        for length in range(min_len, max_len + 1):
            for i in range(10 - length):
                
                num = int(sequence[i:i + length])
                
                if low <= num <= high:
                    result.append(num)
                    
        return result