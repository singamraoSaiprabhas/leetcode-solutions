class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        prefixGcd = []
        current_max = nums[0]
        
        for num in nums:
            if num > current_max:
                current_max = num
            prefixGcd.append(math.gcd(num, current_max))
        prefixGcd.sort()
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum