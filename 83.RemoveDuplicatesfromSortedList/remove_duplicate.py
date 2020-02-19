"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# class ListNode :
# 	def __init__(self, val) :
# 		self.val = val
# 		self.next = None

class Solution :
	def remove_duplicates(self, head) :
		if not head : return head

		prev = dummy = ListNode(-1)
		ptr = head

		while ptr.next :
			if ptr.val == ptr.next.val :
				prev.next = ptr.next
				ptr = ptr.next
			else :
				prev = ptr
				ptr = ptr.next

		return dummy
