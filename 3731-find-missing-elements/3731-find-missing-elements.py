class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        start = min(nums)
        end = max(nums)
        missing_elements = [x for x in range(start, end + 1) if x not in num_set]
        return missing_elements