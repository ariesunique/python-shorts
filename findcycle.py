# You have a singly-linked list ↴ and want to check if it contains a cycle.

# A singly-linked list is built with nodes, where each node has:

# node.next—the next node in the list.
# node.value—the data held in the node. For example, if our linked list stores people in line at the movies, node.value might be the person's name.
# For example:

#   class LinkedListNode(object):

#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# A cycle occurs when a node’s next points back to a previous node in the list. The linked list is no longer linear with a beginning and end—instead, it cycles through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

import unittest


def contains_cycle(first_node):
	if first_node == None:
		return False
	if first_node.next == None:
		return False
	if first_node.next == first_node:
		return True

	
	# initialize fast iterator to third node
	fast_iter = first_node.next.next
	
	# initialize slow iterator to second node
	slow_iter = first_node.next
	
	# loop until one of them reaches the end of the list
	while fast_iter and slow_iter:
		
		# if they point to the same object, then the fast iterator ended up behind the slow one, so there's a loop
		if fast_iter == slow_iter:
			return True
		else:
			# increment the fast iterator by two and the slow iterator by one
			fast_iter = fast_iter.next.next
			slow_iter = slow_iter.next
	
	
	return False


# Tests

class Test(unittest.TestCase):
	class LinkedListNode(object):
		def __init__(self, value, next=None):
			self.value = value
			self.next  = next
			
	def test_linked_list_with_no_cycle(self):
		fourth = Test.LinkedListNode(4)
		third = Test.LinkedListNode(3, fourth)
		second = Test.LinkedListNode(2, third)
		first = Test.LinkedListNode(1, second)
		result = contains_cycle(first)
		self.assertFalse(result)

	def test_cycle_loops_to_beginning(self):
		fourth = Test.LinkedListNode(4)
		third = Test.LinkedListNode(3, fourth)
		second = Test.LinkedListNode(2, third)
		first = Test.LinkedListNode(1, second)
		fourth.next = first
		result = contains_cycle(first)
		self.assertTrue(result)

	def test_cycle_loops_to_middle(self):
		fifth = Test.LinkedListNode(5)
		fourth = Test.LinkedListNode(4, fifth)
		third = Test.LinkedListNode(3, fourth)
		second = Test.LinkedListNode(2, third)
		first = Test.LinkedListNode(1, second)
		fifth.next = third
		result = contains_cycle(first)
		self.assertTrue(result)

	def test_two_node_cycle_at_end(self):
		fifth = Test.LinkedListNode(5)
		fourth = Test.LinkedListNode(4, fifth)
		third = Test.LinkedListNode(3, fourth)
		second = Test.LinkedListNode(2, third)
		first = Test.LinkedListNode(1, second)
		fifth.next = fourth
		result = contains_cycle(first)
		self.assertTrue(result)

	def test_empty_list(self):
		result = contains_cycle(None)
		self.assertFalse(result)

	def test_one_element_linked_list_no_cycle(self):
		first = Test.LinkedListNode(1)
		result = contains_cycle(first)
		self.assertFalse(result)

	def test_one_element_linked_list_cycle(self):
		first = Test.LinkedListNode(1)
		first.next = first
		result = contains_cycle(first)
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main(verbosity=2)
