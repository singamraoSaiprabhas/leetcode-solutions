class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(list(set(arr)))
        rank_map = {}
        for rank, val in enumerate(sorted_unique, 1):
            rank_map[val] = rank
        return [rank_map[num] for num in arr]
