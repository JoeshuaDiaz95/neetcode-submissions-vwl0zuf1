# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)

            self.ans = max(self.ans, L+R)
            return (1 + max(L, R))
        
        dfs(root)
        return self.ans