class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def backtrack(start, path):
            # If we've reached the end of the string, add the current partition to results
            if start == len(s):
                res.append(path[:])
                return
            
            # Explore all possible substrings starting from the current 'start' index
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is a palindrome, add it to the path and recurse
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end, path)
                    # Backtrack to explore other partitions
                    path.pop()
                    
        backtrack(0, [])
        return res