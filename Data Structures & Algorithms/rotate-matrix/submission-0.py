class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 矩陣轉置Transpose
        for r in range(n):
            # c從r開始，只處理對角線右上方，避免重複交換
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]     

        # 每一列水平反轉Reverse
        for r in range(n):
            matrix[r].reverse()   