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
        Inserts a value into the tree
        Args:
            value: int: value to insert into the tree
        Returns:
            None
        '''
        new_node = Node(value)
        if self.root is None :
            self.root = new_node
        else :
            self._insert(self.root, new_node)
            

    def _insert(self, current_node: Node, new_node: Node) -> None:
        '''
        Recursively compare nodes to insert a new one
        Args:
            current: Node: Node to compare
            new_node: Node: Node to insert
        Returns:
            None      
        '''
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(current_node.right, new_node)

    

    def generate_random_tree(self, size: int)-> None:
        '''
        Generate a random search binary tree from a size
        Args:
            size: int: The size of the tree 
        Returns:
            None
        '''
        for i in range(size):
            value : int = getrandbits(32)
            self.insert(value)

    def _in_order(self, node: Node, tree_ordered : list[int])-> None:
        '''
        Parcour the tree in-order recursively
        Args: 
            node: Node: The the node we are at
            tree_ordered: list[int]: the tree in-order
        Returns:
            None
        '''
        if node:
            self._in_order(node.left, tree_ordered)
            tree_ordered.append(node.value)
            self._in_order(node.right, tree_ordered)


    def get_in_order(self)-> list[int]:
        '''
        Get the tree in-order
        Returns:
            tree_ordered: list[int]: the tree in-order
        '''
        tree_ordered : list[int] = []
        self._in_order(self.root, tree_ordered)
        return tree_ordered

    def print_in_order(self)-> None:
        '''
        Print the tree in-order 
        Returns:
            None
        '''
        tree_ordered = self.get_in_order()
        print(tree_ordered)

    def _pre_order(self, node: Node, tree_ordered : list[int])-> None:
        '''
        Parcour the tree pre-order recursively
        Args: 
            node: Node: The the node we are at
            tree_ordered: list[int]: the tree pre-order
        Returns:
            None
        '''
        if node:
            tree_ordered.append(node.value)
            self._pre_order(node.left, tree_ordered)
            self._pre_order(node.right, tree_ordered)

    def get_pre_order(self)-> list[int]:
        '''
        Get the tree pre-order
        Returns:
            tree_ordered: list[int]: the tree pre-order
        '''
        tree_ordered : list[int] = []
        self._pre_order(self.root, tree_ordered)
        return tree_ordered
            
    def print_pre_order(self)-> None:
        '''
        Print the tree pre-order 
        Returns:
            None
        '''
        tree_ordered = self.get_pre_order()
        print(tree_ordered)

    def _post_order(self, node: Node, tree_ordered : list[int])-> None:
        '''
        Parcour the tree post-order recursively
        Args: 
            node: Node: The the node we are at
            tree_ordered: list[int]: the tree post-order
        Returns:
            None
        '''
        if node:
            self._post_order(node.left, tree_ordered)
            self._post_order(node.right, tree_ordered)
            tree_ordered.append(node.value)

    def get_post_order(self)-> list[int]:
        '''
        Get the tree post-order
        Returns:
            tree_ordered: list[int]: the tree post-order
        '''
        tree_ordered : list[int] = []
        self._post_order(self.root, tree_ordered)
        return tree_ordered

    def print_post_order(self)-> None:
        '''
        Print the tree post-order
        Returns:
            None
        '''
        tree_ordered = self.get_post_order()
        print(tree_ordered)

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



