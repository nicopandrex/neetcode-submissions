class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] > target:
                right = middle - 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_matrix = 0
        right_matrix = len(matrix) - 1
        

        while left_matrix <= right_matrix:
            matrix_middle = (left_matrix + right_matrix) // 2

            if matrix[matrix_middle][0] > target:
                right_matrix = matrix_middle - 1

            elif matrix[matrix_middle][-1] < target:
                left_matrix = matrix_middle + 1
            else:
                return self.binarySearch(matrix[matrix_middle], target)
        return False
            

