class Node :
	def __init__(self, val) :
		self.val = val
		self.next = None


class LinkedList :
	def __init__(self, node) :
		self.head = self.tail = node
		self.length = 1

	def addNode(self, value) :
		self.tail.next = Node(value)
		self.tail = self.tail.next
		self.length += 1

	def printLinkedList(self) :
		ptr = self.head
		while ptr :
			print(f'{ptr.val} -> ', end= ' ')
			ptr = ptr.next
		print('\n')
	def reverseLinkedList(self) :
		ptr = self.head
		prev = None

		while ptr.next :
			temp = ptr.next
			ptr.next = prev
			prev = ptr
			ptr = temp
		ptr.next = prev
		self.tail = self.head
		self.head = ptr

if __name__ == '__main__' :
	ll = LinkedList(Node(5))
	ll.addNode(10)
	ll.addNode(15)
	ll.printLinkedList()
	ll.reverseLinkedList()
	print("\nReversed linked list is ")
	ll.printLinkedList()
