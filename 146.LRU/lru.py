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
