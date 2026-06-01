class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                break

        if not (left <= right):
            return False

        index = (left+right) //2
        array = matrix[index]
        inner_r = len(array) - 1
        inner_l = 0
        while inner_l <= inner_r:
            inner_m = (inner_r + inner_l) // 2
            if array[inner_m] == target:
                return True
            elif array[inner_m] > target:
                inner_r = inner_m -1 
            else:
                inner_l = inner_m + 1

        return False

