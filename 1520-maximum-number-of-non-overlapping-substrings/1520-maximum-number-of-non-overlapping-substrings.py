class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        # Helper function to find the valid end of a substring starting at index i
        def get_valid_right(i):
            right = last[s[i]]
            j = i
            while j <= right:
                char = s[j]
                # If a character's first occurrence is before our starting index i, 
                # this is not a valid minimal substring boundary
                if first[char] < i:
                    return -1
                right = max(right, last[char])
                j += 1
            return right
        
        res = []
        last_right = -1
        
        # Step 2: Iterate through the string to greedily pick valid substrings
        for i in range(len(s)):
            # Only start checking from the first occurrence of any character
            if i == first[s[i]]:
                new_right = get_valid_right(i)
                
                if new_right != -1:
                    if i > last_right:
                        # Non-overlapping with the previous valid substring
                        res.append(s[i:new_right + 1])
                    else:
                        # Contained within the previous valid substring, replace it to minimize length
                        res[-1] = s[i:new_right + 1]
                    last_right = new_right
                    
        return res