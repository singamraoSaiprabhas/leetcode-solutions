class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        
        if k == 0:
            return grid
            
        flat_list = []
        for row in grid:
            flat_list.extend(row)
        rotated_list = flat_list[-k:] + flat_list[:-k]
        result = []
        for i in range(0, total_elements, n):
            result.append(rotated_list[i : i + n])
            
        return result