# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # 左右各自節點後面有幾層
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 自己root也是一層，因此+1
        return max(left_depth, right_depth)+1
