class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start_index, current_sum, current_combination):
            if current_sum == target:
                res.append(current_combination[:])
                return
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                current_combination.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], current_combination)
                current_combination.pop()                
        backtrack(0, 0, [])
        return res