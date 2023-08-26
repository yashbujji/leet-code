class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for i in (grid[1:]):
            if i == grid[0] or i == [x^1 for x in grid[0]]:
                continue
            else:
                return False
        return True


        