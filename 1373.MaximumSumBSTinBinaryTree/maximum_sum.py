'''
Given a binary tree root, the task is to return the maximum
sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1 :
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
Example 4:

Input: root = [2,1,3]
Output: 6
Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7


Constraints:

Each tree has at most 40000 nodes..
Each node's value is between [-4 * 10^4 , 4 * 10^4].

 '''


'''
class TreeNode :
	def __init__(self, val) :
		self.val = val
		self.left = None
		self.right = None
'''

class Solution :
	def __init__(self) :
		self._max_sum = 0

	def maxSumBST(self, root) :
		self._find_sum_helper(root)
		return self._max_sum

	def _find_sum_helper(self, node) :
		if not node : return 0, True
		left_sum, left = self._find_sum_helper(node.left)
		right_sum, right = self._find_sum_helper(node.right)

		local_sum = node.val

		if node.left :
			if node.left.val >= node.val :
				return 0, False

		if node.right :
			if node.right.val <= node.val :
				return 0, False

		if left and right :
			local_sum += left_sum + right_sum
			self._max_sum = max(self._max_sum, local_sum)

			return local_sum, True

		return node.val, False

