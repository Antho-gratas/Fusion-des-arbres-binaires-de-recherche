from typing import List
from tree.tree import Tree

class MergeBST():
    '''
    Class to merge two binary search trees
    '''

    def __init__(self, tree1: Tree, tree2: Tree)-> None:
        self.tree1 = tree1
        self.tree2 = tree2

    def merge(self, order1: str, order2: str) -> Tree:
        '''
        Merge two binary search trees based on specified traversal orders.
        Args:
            order1: str: The traversal order for tree1 (in-order, pre-order, post-order)
            order2: str: The traversal order for tree2 (in-order, pre-order, post-order)
        Returns:
            Tree: The new merged binary search tree
        '''
        tree_ordered_1 = self._get_values_by_order(self.tree1, order1)
        tree_ordered_2 = self._get_values_by_order(self.tree2, order2)
        
        merged_values = self._merge_sorted_lists(tree_ordered_1, tree_ordered_2)

        merged_tree = Tree(None)
        for value in merged_values:
            merged_tree.insert(value)

        return merged_tree

    def _get_values_by_order(self, tree: Tree, order: str) -> List[int]:
        '''
        Get the node values of a tree based on the specified order.
        Args:
            tree: Tree: The tree to traverse
            order: str: The traversal order ('in-order', 'pre-order', 'post-order')
        Returns:
            List[int]: A list of node values in the specified order
        '''
        if order == 'in-order':
            return tree.get_in_order()
        elif order == 'pre-order':
            return tree.get_pre_order()
        elif order == 'post-order':
            return tree.get_post_order()
        else:
            raise ValueError(f"Invalid order: {order}")

    def _merge_sorted_lists(self, list1: List[int], list2: List[int]) -> List[int]:
        '''
        Merge two sorted lists into one sorted list.
        Args:
            list1: List[int]: The first sorted list
            list2: List[int]: The second sorted list
        Returns:
            List[int]: The merged sorted list
        '''
        merged_list = []
        i, j = 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1

        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

        return merged_list
    
    def merge_n_trees(self, trees: List[Tree], order1: str, order2: str)-> Tree:
        '''
        Merge n binary search trees.
        Args:
            trees: List[Tree]: The list of trees to merge
            order1: str: The traversal order for tree1 (in-order, pre-order, post-order)
            order2: str: The traversal order for tree2 (in-order, pre-order, post-order)
        Returns:
            Tree: The new merged binary search tree
        '''

        tree_merged : Tree = trees[0]
        
        for i in range(1, len(trees)):
            self.tree1 = tree_merged
            self.tree2 = trees[i]
            tree_merged = self.merge(order1, order2)

        return tree_merged


        
        
    