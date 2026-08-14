# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 最大直徑
        self.max_diameter = 0

        def get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 左右邊的深度
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            # 兩邊的深度加起來，也就是經過自己節點的路徑
            current_diameter = left_depth + right_depth

            # 更新最大路徑
            self.max_diameter = max(self.max_diameter, current_diameter)

            # 回報深度
            return max(left_depth, right_depth) + 1
        
        get_depth(root)

        return self.max_diameter
