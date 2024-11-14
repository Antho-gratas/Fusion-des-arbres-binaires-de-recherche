from typing import List
from tree.tree import Tree
from node.node import Node
from collections import deque

class MergeBST:
    '''Merge Binary search tree class'''
    
    def __init__(self, tree1: Tree, tree2: Tree) -> None:
        self.tree1 = tree1
        self.tree2 = tree2

    def merge(self, order1: str, order2: str) -> Tree:
        '''
        Merges two binary search trees into a single tree.
        
        Args:
            order1: str: Traversal type for the first tree (in-order, pre-order, post-order).
            order2: str: Traversal type for the second tree (in-order, pre-order, post-order).
        
        Returns:
            Tree: A new binary search tree containing all elements from both original trees.
        '''
        
        merged_tree = Tree()   
        
        iterator1 = self.get_iterator(self.tree1, order1)
        iterator2 = self.get_iterator(self.tree2, order2)
        
        value1 = next(iterator1, None)
        value2 = next(iterator2, None)

        while value1 is not None or value2 is not None:
            if value2 is None or (value1 is not None and value1 <= value2):
                merged_tree.insert(value1)
                value1 = next(iterator1, None)
            else:
                merged_tree.insert(value2)
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

    def in_order_iter(self, node: Node):
        '''
        In-order traversal iterator
        '''
        if node is not None:
            yield from self.in_order_iter(node.left)
            yield node.value
            yield from self.in_order_iter(node.right)

    def pre_order_iter(self, node: Node):
        '''
        Pre-order traversal iterator
        '''
        if node is not None:
            yield node.value
            yield from self.pre_order_iter(node.left)
            yield from self.pre_order_iter(node.right)

    def post_order_iter(self, node: Node):
        '''
        Post-order traversal iterator
        '''
        if node is not None:
            yield from self.post_order_iter(node.left)
            yield from self.post_order_iter(node.right)
            yield node.value

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



        
        
    