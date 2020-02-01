"""Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4"""



# implementation using simple dictionary. Since python 3.7 python dictionaries
# are ordered by the insertion of the keys

class LRU :
	def __init__(self, capacity) :
		self.capacity = capacity
		self.cache = dict()

	def get(self, key) :
		if key not in self.cache :
			return -1

		# if key is found, move the key to the end of the
		# dict
		self.cache[key] = self.cache.pop(key)
		return self.cache[key]

	def put(self, key, value) :
		if key in self.cache :
			# use the key in the LRU
			self.cache[key] = self.cache.pop(key)
		self.cache[key] = value
		if (len(self.cache)) > self.capacity :
			for key in self.cache :
				self.cache.pop(key)
				break

# Takes O(1) time for put and get operations since we use dictionary for the design
# O(capacity) space


# method for using the OrderedDict
# this method also has same complexity as using the usual dictionary
# notice how we pass OrderedDict object to out LRU class -> inheritance ?

from collections import OrderedDict
class LRU2(OrderedDict) :
	def __init__(self, capacity) :
		self.capacity = capacity

	def get(self, key) :
		if key not in self :
			return -1

		self.move_to_end(key)
		return self[key]

	def put(self, key, value) :
		if key in self :
			self.move_to_end(key)

		self[key] = value
		if len(self) > self.capacity :
			self.popitem(last = False)


# approach using doubly linked list and dictionary

class DoublLinkedNode :
	def __init__(self) :
		self.key = 0
		self.value = 0
		self.next = None
		self.prev = None

class LRU3 :
	def __init__(self, capacity) :
		self.capacity = capacity
		self.size = 0
		self.cache = dict() # stores the reference to the DoublyNode object

		self.head = DoublLinkedNode()
		self.tail = DoublLinkedNode()

		self.head.next = self.tail
		self.tail.prev = self.head

	# new node is always added to the head of the Linked List
	def _add_node(self, node) :
		node.next = self.head.next
		node.prev = self.head

		self.head.next.prev = node
		self.head.next = node

	# remove the node and add it again
	# although we could move the node from tail to the head
	def _move_to_head(self, node) :
		self._remove_node(node)
		self._add_node(node)

	# this method deletes any node from any location
	def _remove_node(self, node) :
		prev = node.prev
		nextPtr = node.next

		prev.next = nextPtr
		nextPtr.prev = prev

	# use the remove node method
	# return the node
	def _pop_tail(self) :
		res = self.tail.prev

		self._remove_node(res)
		return res

	def get(self, key) :
		node = self.cache.get(key, None)

		# if we don't have such node
		if not Node :
			return -1

		# if we have the node
		# before returning it, make it newly used node
		# mode it to the head of the list
		self._move_to_head(node)
		return node.val

	def put(self, key, value) :
		node = self.cache.get(key, None)

		# if key does not exit
		# create the Doubly Node
		# place the new node into the cache dictionary
		# increase the size of our LRU cache
		# chech if the cache is overflown
		# if so, delete the LRU

		if not node :
			newNode = DoublLinkedNode()
			newNode.key = key
			newNode.value = value

			self.cache[key] = newNode
			self._add_node(newNode)
			self.size += 1

			if self.size > self.capacity :
				# remove the LRU node which is the node prev to Tail
				tail = self._pop_tail()
				def self.cache[tail.key]
				self.size -= 1

		# if node exists
		# update the value
		# move the value to the beginning of the list
			# remove the node
			# add the node
		else :
			moveMe = self.cache[key]
			self._move_to_head(moveMe)
			moveMe.value = value
