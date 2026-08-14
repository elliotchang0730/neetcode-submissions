# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 空節點回傳Nome
        if not root:
            return None
        
        # 左右反轉交換
        root.left, root.right = root.right, root.left

        # 下面的子樹也交換
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root