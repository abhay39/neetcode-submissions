class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
        return False