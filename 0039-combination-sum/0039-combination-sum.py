class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        res = []
        










        def backtrack(start: int, path: List[int], remain: int):
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                
                path.append(candidates[i])
                backtrack(i, path, remain - candidates[i])
                path.pop()  
                
        backtrack(0, [], target)
        return res