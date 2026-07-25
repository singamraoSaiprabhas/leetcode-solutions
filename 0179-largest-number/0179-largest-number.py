class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0
        nums_str.sort(key=cmp_to_key(compare))
        largest_num = "".join(nums_str)
        if largest_num[0] == "0":
            return "0"
            
        return largest_num