class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:  # Ignore seats 1 and 10
                occupied[r] |= (1 << c)

        ans = (n - len(occupied)) * 2

        LEFT = 60
        RIGHT = 960
        MIDDLE = 240

        for mask in occupied.values():
            left_open = (mask & LEFT) == 0
            right_open = (mask & RIGHT) == 0
            middle_open = (mask & MIDDLE) == 0

            if left_open and right_open:
                ans += 2
            elif left_open or right_open or middle_open:
                ans += 1

        return ans