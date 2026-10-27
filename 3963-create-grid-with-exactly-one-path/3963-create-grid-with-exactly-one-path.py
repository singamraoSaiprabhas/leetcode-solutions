class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            if i == 0:
                # The entire first row is free cells
                grid.append("." * n)
            else:
                # Subsequent rows are obstacles except for the last column
                grid.append("#" * (n - 1) + ".")
                
        return grid