class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        # 1. Collect coordinates of all 1s in both images
        points1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        points2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        # If either matrix has no 1s, overlap is 0
        if not points1 or not points2:
            return 0

        # 2. Count the frequency of each translation vector (dr, dc)
        shift_counts = defaultdict(int)
        for r1, c1 in points1:
            for r2, c2 in points2:
                shift_vector = (r2 - r1, c2 - c1)
                shift_counts[shift_vector] += 1

        # 3. The maximum count represents the largest overlap
        return max(shift_counts.values())