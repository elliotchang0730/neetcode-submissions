class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix:
            return []
            
        res = []
        
        # 建立四個邊界指標
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        # 只要四個邊界沒有交錯，就繼續繞圈
        while left <= right and top <= bottom:
            
            # 向右走，走完最上面那一列的所有欄
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1 # 上邊界往下縮一格
            
            # 向下走，走完最右邊那一欄的所有列
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1 # 右邊界往左縮一格
            
            # 因為上面top或right已經變動過，
            # 必須重新確認邊界是否還成立，避免長方形矩陣重複讀取
            if not (left <= right and top <= bottom):
                break
                
            # 向左走，走完最下面那一列的所有欄
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1 # 下邊界往上縮一格
            
            # 向上走，走完最左邊那一欄的所有列
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1 # 左邊界往右縮一格
            
        return res
