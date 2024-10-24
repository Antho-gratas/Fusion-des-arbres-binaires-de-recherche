from typing import List
from tree.tree import Tree

class MergeBST:
    '''
    Class to merge two binary search trees
    '''

    def __init__(self, tree1: Tree, tree2: Tree) -> None:
        self.tree1 = tree1
        self.tree2 = tree2

    def merge(self, order1: str, order2: str) -> Tree:
        '''
        Merge two binary search trees based on specified traversal orders.
        Args:
            order1: str: The traversal order for tree1 (in-order, pre-order, post-order)
            order2: str: The traversal order for tree2 (in-order, pre-order, post-order)
        Returns:
            Tree: The new balanced binary search tree
        '''
        values1 = self._get_values_by_order(self.tree1, order1)
        values2 = self._get_values_by_order(self.tree2, order2)
        
        merged_values = self._concat_and_sort(values1, values2)
        
        return self._sorted_list_to_balanced_bst(merged_values)

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

    def _concat_and_sort(self, list1: List[int], list2: List[int]) -> List[int]:
        ''' 
        Concatenate two lists and return a single sorted list.
        Args:
            list1: List[int]: The first list
            list2: List[int]: The second list
        Returns:
            List[int]: The merged sorted list
        '''
        return sorted(list1 + list2)

    def _sorted_list_to_balanced_bst(self, sorted_values: List[int]) -> Tree:
        '''
        Convert a sorted list to a balanced binary search tree iteratively.
        '''
        if not sorted_values:
            return None
        
        tree = Tree()  
        queue = [(0, len(sorted_values) - 1)]  

        while queue:
            start, end = queue.pop(0)
            
            if start > end:
                continue
            
            mid = (start + end) // 2
            tree.insert(sorted_values[mid]) 

            queue.append((start, mid - 1))
            queue.append((mid + 1, end)) 
        return tree


    def merge_n_trees(self, trees: List[Tree], order1: str, order2: str) -> Tree:
        '''
        Merge n binary search trees.
        Args: 
            trees: List[Tree]: A list of trees to merge
            order: str: The traversal order for each tree (in-order, pre-order, post-order)
        Return:
            Tree: The merged tree
        '''
        merged_tree = trees[0]

        for i in range(1, len(trees)):
            self.tree1 = merged_tree
            self.tree2 = trees[i]
            merged_tree = self.merge(order1, order2)

        return merged_tree
