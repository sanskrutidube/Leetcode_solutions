# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum=0
        def inorder(root):
            if not root:
                return 0
            if low <= root.val <= high:
                self.sum+=root.val
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        return (self.sum)
        
