from node.node import Node
from random import *

class Tree():
    '''
    Binary search tree class
    '''

    def __init__(self, root: Node = None)-> None:
        self.root = root
    
    def insert(self, value: int)-> None:
        '''
        Inserts a value into the tree iteratively
        Args:
            value: int: value to insert into the tree
        Returns:
            None
        '''
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        return
                    else:
                        current = current.right

    def generate_random_tree(self, size: int)-> None:
        '''
        Generate a random search binary tree of size `size` iteratively
        Args:
            size: int: The size of the tree 
        Returns:
            None
        '''
        for i in range(size):
            value = getrandbits(32) 
            self.insert(value)

    def _in_order(self):
        '''
        Get the tree in-order 
        Returns:
            None
        '''
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def get_in_order(self):
        '''
        Get the tree in-order 
        Returns:
            None
        '''
        return self._in_order()

    def print_in_order(self):
        '''
        Print the tree in-order 
        Returns:
            None
        '''
        print(self._in_order())
        

    def _pre_order(self):
        '''
        Get the tree pre-order 
        Returns:
            result: list[int]: The list of node values in pre-order
        '''
        result = []
        if self.root is None:
            return result
        
        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.value)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    def get_pre_order(self):
        '''
        Get the tree pre-order 
        Returns:
            list[int]: The list of node values in pre-order
        '''
        return self._pre_order()

    def print_pre_order(self):
        '''
        Print the tree in pre-order 
        Returns:
            None
        '''
        print(self._pre_order())

    def _post_order(self):
        '''
        Get the tree post-order 
        Returns:
            result: list[int]: The list of node values in post-order
        '''
        result = []
        if self.root is None:
            return result

        stack = []
        current = self.root
        last_visited = None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                # If the right subtree exists and has not been processed
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    result.append(peek_node.value)
                    last_visited = stack.pop()

        return result

    def get_post_order(self):
        '''
        Get the tree post-order 
        Returns:
            list[int]: The list of node values in post-order
        '''
        return self._post_order()

    def print_post_order(self):
        '''
        Print the tree in post-order 
        Returns:
            None
        '''
        print(self._post_order())

