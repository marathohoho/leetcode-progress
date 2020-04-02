'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(N) time and O(N) space - for recursive calls
class Solution:
	def __init__(self) :
		self.lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		self.helper(root, p, q)
		return self.lca

	def helper(self, node, p, q) :
		if not node : return False

		left = self.helper(node.left, p, q)
		right = self.helper(node.right, p, q)

		# check the current node value
		# if it is equal to either of the two nodes passed,
		# then it has to be the  candidate for LCA

		mid = node.val == p.val or node.val == q.val

		if mid + right + left >= 2 :
			self.lca = node

		return mid + right + left

