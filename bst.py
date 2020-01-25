# --------------------------
#
# Determine if a given tree is a valid binary search tree.
# A binary search tree is one such that the root node is greater than
# all the elements to its left, and less than all the elements to its
# right. Each subtree must also be a valide binary search tree.
#
# This was part of an algorithms practice challenge. Only the test cases 
# were given.
# 
# This code makes use of the fact that an inorder traversal of a valid 
# binary search results in an ordered list of items. This may not be the
# most efficient, but it is easy to understand and implement. 
#
# In terms of time complexity, the time to traverse the tree is O(n). 
# We will need additional time to sort the list. Python uses Timsort 
# which runs in O(n) in the best case. If the tree is a valid binary 
# search tree, it will be already in order when we run Timsort 
# (best case) and will sort in O(n) time. If the tree is not a valid 
# binary search tree, there will be a sort which can approach O(n log n) 
# in the worst case. So the time complexity for this approach is 
# O(n) on average and O(n) + O(n log n) in the worst case.
#
# --------------------------


import unittest
import pytest


def inorder_traversal(root):
    if not root:
        return []
    
    if not root.left and not root.right:
        return [root.value]
    
    inorder = []
    inorder.extend( inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right))
    return inorder


def is_binary_search_tree(root):
    if not root:
        return False
    
    inorder = inorder_traversal(root)

    return inorder == sorted(inorder)
        
        
# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right
        
        def __repr__(self):
            return str(self.value)
    
    
    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)
        
      
    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)
    
    
    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    


    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)


    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)
    

    def test_simple_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_simple_full_tree_fail(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(40)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)        
     
    def test_fail_left_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(25)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)
        
    def test_fail_recursive_left_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(40)
        left.left.insert_left(25)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)
        
        
    def test_fail_right_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(40)
        right.insert_left(100)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)
        
#unittest.main(verbosity=2)