from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R*C-1
        print(R,C,r,'r')
        while l <= r:
            mid = l + (r-l)//2
            print(mid)
            row, col = mid // C, mid % C
            print(f"Searching at position ({row}, {col}), Value: {matrix[row][col]}")
            
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True

        return False

# Test cases
s = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(f"Search {target} in matrix: {s.searchMatrix(matrix, target)}")

# target = 13
# print(f"Search {target} in matrix: {s.searchMatrix(matrix, target)}")
