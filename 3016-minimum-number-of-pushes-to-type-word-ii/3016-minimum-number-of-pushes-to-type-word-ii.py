class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        sorted_frequencies = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        for i, count in enumerate(sorted_frequencies):
            pushes_per_char = (i // 8) + 1
            total_pushes += count * pushes_per_char
            
        return total_pushes