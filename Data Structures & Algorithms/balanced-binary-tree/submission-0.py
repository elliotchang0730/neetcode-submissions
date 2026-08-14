# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_depth = get_depth(node.left)
            # 3. 如果左邊深度收到-1
            if left_depth == -1:
                return -1

            right_depth = get_depth(node.right)
            # 4. 如果右邊深度收到-1
            if right_depth == -1:
                return -1
            
            # 1.如果兩邊相差大於1，代表不平衡，這裡令發生這個狀況回傳-1
            if abs(left_depth - right_depth) > 1:
                return -1
            # 2. 如果平衡則回傳現在的層回去
            return max(left_depth, right_depth) + 1
        
        # 5. 如果有收到-1
        return get_depth(root) != -1
            