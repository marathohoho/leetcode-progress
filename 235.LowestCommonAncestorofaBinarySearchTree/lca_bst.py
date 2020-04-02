"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # apply rules of a Binary Search Tree (left < root <= right)
        # based on this rule if p < root.val <= q then root is the LCA
        # if root.val is larger than both p and q, then recurse into the left subtree
        # if root.val is smaller than then recurse into the right subtree

		return self.helper(root, p.val, q.val)

	def helper(self, node, p, q) :
		if node.val > p and node.val > q :
			return self.helper(node.left, p, q)
		elif node.val < p and node.val < q :
			return self.helper(node.right, p, q)
		else :
			return node
