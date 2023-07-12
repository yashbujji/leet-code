class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,col=len(matrix),len(matrix[0])
        for row in matrix:
            left,right=0,len(row)-1
            while left<=right:
                mid=(left+right)//2
                if row[mid]==target:
                    return True
                if row[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
        return False
