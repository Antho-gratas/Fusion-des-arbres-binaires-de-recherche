from typing import List
from avltree.avltree import TreeAVL
from avlnode.avlnode import NodeAVL
from typing import Iterator

class MergeAVL:
    '''Merge AVL Binary search tree class'''
    
    def __init__(self, tree1: TreeAVL, tree2: TreeAVL)-> None:
        self.tree1: TreeAVL = tree1
        self.tree2: TreeAVL = tree2

    def merge(self, order1: str, order2: str)-> TreeAVL:
        '''
        Merges two AVL binary search trees into a single tree.
        
        Args:
            order1: str: Traversal type for the first tree (in-order, pre-order, post-order).
            order2: str: Traversal type for the second tree (in-order, pre-order, post-order).
        
        Returns:
            TreeAVL: A new AVL binary search tree containing all elements from both original trees.
        '''
        
        merged_tree: TreeAVL = TreeAVL()   
        
        iterator1: Iterator[int] = self.get_iterator(self.tree1, order1)
        iterator2: Iterator[int] = self.get_iterator(self.tree2, order2)
        
        value1: int = next(iterator1, None)
        value2: int = next(iterator2, None)

        while value1 is not None or value2 is not None:
            if value2 is None or (value1 is not None and value1 <= value2):
                merged_tree.insert(value1)
                value1 = next(iterator1, None)
            else:
                merged_tree.insert(value2)
                value2 = next(iterator2, None)

        return merged_tree

    def get_iterator(self, tree: TreeAVL, order: str)-> Iterator[int]:
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

    def in_order_iter(self, node: NodeAVL)-> Iterator[int]:
        '''
        In-order traversal iterator.
        '''
        stack: list[NodeAVL] = [] 
        current: NodeAVL = node  
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            yield current.value
            current = current.right

    def pre_order_iter(self, node: NodeAVL)-> Iterator[int]:
        '''
        Pre-order traversal iterator.
        '''
        stack: list[NodeAVL] = [node]
        while stack:
            current = stack.pop()
            if current:
                yield current.value
                stack.append(current.right)
                stack.append(current.left)

    def post_order_iter(self, node: NodeAVL)-> Iterator[int]:
        '''
        Post-order traversal iterator.
        '''
        stack1: list[NodeAVL] = [node]
        stack2: list[NodeAVL] = []
        while stack1:
            current: NodeAVL = stack1.pop()
            if current:
                stack2.append(current)
                stack1.append(current.left)
                stack1.append(current.right)
        while stack2:
            yield stack2.pop().value

    def merge_n_trees(self, trees: List[TreeAVL], order1: str, order2: str) -> TreeAVL:
        '''
        Merges multiple AVL binary search trees.
        
        Args:
            trees: List[TreeAVL]: List of trees to merge.
            order1: str: Traversal order for the first tree.
            order2: str: Traversal order for the second tree.
        
        Returns:
            TreeAVL: A new AVL binary search tree that merges all given trees.
        '''
        tree_merged: TreeAVL = trees[0]
        for i in range(1, len(trees)):
            self.tree1 = tree_merged
            self.tree2 = trees[i]
            tree_merged = self.merge(order1, order2)

        return tree_merged



        
        
    