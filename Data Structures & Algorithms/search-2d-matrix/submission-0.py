class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # Rows
        n = len(matrix[0])  # Cols
        
        # 定義虛擬一維陣列的左右邊界指標
        left, right = 0, (m * n) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 將一維的mid索引轉換回二維矩陣的(row, col)座標
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True       # 找到目標
            elif mid_val < target:
                left = mid + 1    # 目標值較大，往右半邊找
            else:
                right = mid - 1   # 目標值較小，往左半邊找
                
        return False