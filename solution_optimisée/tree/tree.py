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

    def print_tree(self):
        '''
        Display the binary search tree in a graphical format like:
        '''
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """
        Returns list of strings, width, height, and horizontal coordinate of the root.
        """
        # Base case: No node
        if node is None:
            return [], 0, 0, 0
        
        if node.right is None and node.left is None:
            line = str(node.value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n // 2

        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.value)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = str(node.value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [a + u * ' ' + b for a, b in zipped_lines]
        return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


