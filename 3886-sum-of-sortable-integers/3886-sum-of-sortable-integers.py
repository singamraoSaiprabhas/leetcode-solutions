class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        sorted_nums = sorted(nums)
        
        for k in range(1, n + 1):
            # Only consider divisors of n
            if n % k != 0:
                continue
                
            possible = True
            
            # Process each independent chunk of size k
            for i in range(0, n, k):
                sub = nums[i : i+k]
                expected = sorted_nums[i : i+k]
                
                # Find the number of 'drops' to locate the exact shift point
                drops = 0
                drop_idx = -1
                
                for j in range(k - 1):
                    if sub[j] > sub[j+1]:
                        drops += 1
                        drop_idx = j
                        # More than 1 drop means it can't be a valid cyclic shift
                        if drops > 1:
                            break
                
                # Evaluate based on the drop count
                if drops == 0:
                    # No drops, it should be identical to the expected sorted chunk
                    if sub != expected:
                        possible = False
                        break
                elif drops == 1:
                    # One drop, the shift exactly aligns with drop_idx + 1
                    shift = drop_idx + 1
                    if sub[shift:] + sub[:shift] != expected:
                        possible = False
                        break
                else:
                    # Multiple drops fail automatically
                    possible = False
                    break
                    
            if possible:
                ans += k
                
        return ans