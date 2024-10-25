from typing import List
from tree.tree import Tree
from node.node import Node
from collections import deque

class MergeBST:
    def __init__(self, tree1: Tree, tree2: Tree):
        # Initialize the two binary search trees to be merged
        self.tree1 = tree1
        self.tree2 = tree2

    def merge(self, order1: str, order2: str) -> Tree:
        '''
        Merges two binary search trees into a single balanced tree.
        
        Args:
            order1: str: Traversal type for the first tree (in-order, pre-order, post-order).
            order2: str: Traversal type for the second tree (in-order, pre-order, post-order).
        
        Returns:
            Tree: A new balanced binary search tree containing all elements from both original trees.
        '''
        
        merged_tree = Tree()  
        queue = deque()       
        
        iterator1 = self.get_iterator(self.tree1, order1)
        iterator2 = self.get_iterator(self.tree2, order2)
        
        value1 = next(iterator1, None)
        value2 = next(iterator2, None)

        def insert_balanced(tree, value):
            queue.append(tree.root) if tree.root else setattr(tree, 'root', Node(value))
            while queue:
                current = queue.popleft()
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        queue.append(current.left)
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    else:
                        queue.append(current.right)

        while value1 is not None or value2 is not None:
            if value2 is None or (value1 is not None and value1 <= value2):
                insert_balanced(merged_tree, value1)
                value1 = next(iterator1, None)
            else:
                insert_balanced(merged_tree, value2)
                value2 = next(iterator2, None)

        return merged_tree

    def get_iterator(self, tree: Tree, order: str):
        '''
        Returns an iterator based on the specified traversal order.
        '''
        if order == "in-order":
            return self.in_order_iter(tree.root)
        elif order == "pre-order":
            return self.pre_order_iter(tree.root)
        elif order == "post-order":
            return self.post_order_iter(tree.root)
        else:
            raise ValueError("Invalid traversal order specified")

    def in_order_iter(self, node):
        '''
        In-order traversal iterator.
        '''
        stack, current = [], node
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            yield current.value
            current = current.right

    def pre_order_iter(self, node):
        '''
        Pre-order traversal iterator.
        '''
        stack = [node]
        while stack:
            current = stack.pop()
            if current:
                yield current.value
                stack.append(current.right)
                stack.append(current.left)

    def post_order_iter(self, node):
        '''
        Post-order traversal iterator.
        '''
        stack1, stack2 = [node], []
        while stack1:
            current = stack1.pop()
            if current:
                stack2.append(current)
                stack1.append(current.left)
                stack1.append(current.right)
        while stack2:
            yield stack2.pop().value

    def merge_n_trees(self, trees: List[Tree], order1: str, order2: str) -> Tree:
        '''
        Merges multiple binary search trees.
        
        Args:
            trees: List[Tree]: List of trees to merge.
            order1: str: Traversal order for the first tree.
            order2: str: Traversal order for the second tree.
        
        Returns:
            Tree: A new binary search tree that merges all given trees.
        '''
        tree_merged = trees[0]
        for i in range(1, len(trees)):
            self.tree1 = tree_merged
            self.tree2 = trees[i]
            tree_merged = self.merge(order1, order2)

        return tree_merged



        
        
    