class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        s= [value for row in grid for value in row]
        s.sort()
        return s[math.ceil(len(s)/2)-1]
