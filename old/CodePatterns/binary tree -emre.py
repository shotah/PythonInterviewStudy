# https://emre.me/data-structures/binary-tree/


# Implementation of Binary Tree
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data
        

# insert_left function
def insert_left(self, value):
    if self.left is None:
        self.left = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.left = self.left
        self.left = new_node
        
# insert_right function
def insert_right(self, value):
    if self.right is None:
        self.right = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.right = self.right
        self.right = new_node

# Implementation Summary
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_value(self, value):
        self.root = value

    def get_root_value(self):
        return self.root

# Binary Tree Traversals
# Pre-order Traversal
def pre_order(self):
    print(self.value)

    if self.left_child:
        self.left_child.pre_order()

    if self.right_child:
        self.right_child.pre_order()
        
# In-order Traversal
def in_order(self):
    if self.left:
        self.left.in_order()

    print(self.root)

    if self.right:
        self.right.in_order()
        
# Post-order Traversal
def post_order(self):
    if self.left:
        self.left.post_order()

    if self.right:
        self.right.post_order()

    print(self.root)
    
# Example

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left
b_node.insert_right('d')

c_node = a_node.right
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right
e_node = c_node.left
f_node = c_node.right

print(a_node.root)  # a
print(b_node.root)  # b
print(c_node.root)  # c
print(d_node.root)  # d
print(e_node.root)  # e
print(f_node.root)  # f

print(a_node.pre_order())  # abdcef
print(a_node.in_order())  # bdaecf
print(a_node.post_order())  # dbefca
