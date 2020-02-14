"""

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.

"""
class MaxStack :
	def __init__(self) :
		self.stack = []

	def push(self, x) :
		curr_max = self.peekMax()
		if curr_max == None or curr_max < x :
			x = curr_max
		self.stack.append((x, curr_max))

	def pop(self) :
		if self.stack :
			return self.stack.pop()[0]
		return None

	def top(self) :
		if self.stack :
			return self.stack[-1][0]
		return None

	def peekMax(self) :
		if self.stack :
			return self.stack[-1][1]
		return None

	def popMax(self) :
		if self.stack :
			temp = []
			stack_max = self.peekMax()
			while self.top() != stack_max :
				temp.append(self.pop())
			returned_max = self.pop()

			for element in reversed(temp) :
				self.push(element)

			return returned_max
