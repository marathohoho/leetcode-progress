"""
Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
"""

# definition of node class
class Node :
	def __init__(self, val) :
		self.val = val
		self.left = None
		self.right = None

class Solution :
	def __init__(self) :
		self._product = 0
		self._total_sum = 0

	 def maxProduct(self, root: TreeNode) -> int:
		self._total_sum = self.calcSum(root)
		self.calcSum(root)

		return self._total_sum % (10 ** 9 + 7)

	def calcSum(self, root) :
		if not root : return 0
		left_sum, right_sum = self.calcSum(root.left), self.calcSum(root.right)
		self._product = max(self._product, left_sum * (self._total_sum - left_sum), right_sum * (self._total_sum - right_sum))

		return left_sum  + right_sum + root.val

