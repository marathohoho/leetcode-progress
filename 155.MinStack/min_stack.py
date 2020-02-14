"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack :
	def __init__(self) :
		self.stack = []

	def push(self, x) :
		curr_min = self.getMin()
		if curr_min == None or x < curr_min :
			curr_min = x
		self.stack.append((x, curr_min))

	def pop(self) :
		if self.stack :
			return self.stack.pop()[0]
		return None

	def top(self) :
		if self.stack :
			return self.stack[-1][0]
		return None

	def getMin(self) :
		if self.stack :
			return self.stack[-1][1]
		return None
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__" :
	my_stack = MinStack()
	my_stack.push(100)
	my_stack.push(0)
	my_stack.push(123)
	my_stack.push(-1123)

	print(my_stack.getMin())
