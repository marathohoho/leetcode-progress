import random
class RandomizedSet :
	def __init__(self) :
		# dict keeps the key : value pairs (value : its position)
		self.dct = dict()
		# list that keeps the actual values at positions mentioned in the dict
		self.lst = list()
	def insert(self, val) :
		"""
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
		if val in self.dict :
			return False

		self.dict[val] = len(self.lst)
		self.lst.append(val)

		return True

	def remove(self, val) :
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
		if val in self.dct :
			last_element_from_list, index_where_to_place = self.lst[-1], self.dct[val]
			self.lst[index_where_to_place], self.dct[last_element_from_list] = last_element_from_list, index_where_to_place

			self.lst.pop()
			del self.dct[val]

			return True

		return False

	def getRandom(self) :
        """
        Get a random element from the set
        """
		# choice method outputs a random element from the iterable (list) in O(1)
		return random.choice(self.lst)
