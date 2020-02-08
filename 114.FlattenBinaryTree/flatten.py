class Node :
	def __init__(self, val) :
		self.val = val
		self.left = None
		self.right = None

	def flatten(self) :
		return self._helper(self.root)

	 def _helper(self, node) :
		if node == None :
			 return

		self._helper(node.left) or self._helper(node.right)

		if node.left :
			temp = node.left
			while temp.right :
				temp = temp.right

			temp.right = node.right
			node.right = node.left
			node.left = None
		return
