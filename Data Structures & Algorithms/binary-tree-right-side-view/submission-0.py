# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        right_view = []
        q = deque([root])

        while q:
            length_level = len(q)

            for i in range(length_level):
                node = q.popleft()

                if i == (length_level - 1):
                    right_view.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return right_view



        