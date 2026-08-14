# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 如果大樹為空
        if not root:
            return False
        # 如果小樹為空
        if not subRoot:
            return True
        # 如果大樹小樹一模一樣
        if self.isSameTree(root, subRoot):
            return True
        
        # 如果不完全一樣，左邊找或是右邊找，有找到就成功
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        