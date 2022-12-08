# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
		return self.helper(root1)==self.helper(root2)       
	def helper(self,root):
		res=[]
		if not root:
			return []
		if not root.left and not root.right:
			res.append(root.val)
		res+=self.helper(root.left)
		res+=self.helper(root.right)
		return res
