from typing import List
from tree.tree import Tree
from merge.merge import MergeBST
from node.node import Node

class Solution:
    def __init__(self, tree1: Tree, tree2: Tree):
        self.tree1 = tree1
        self.tree2 = tree2
        self.merge = MergeBST(tree1, tree2)
    
    def merge_trees(self)-> Tree:
        return self.merge.merge("in-order", "pre-order")
    
    def merge_n_trees(self, trees: List[Tree])-> Tree:
        return self.merge.merge_n_trees(trees, "in-order", "pre-order")

    def run(self):
        print('Merging two trees')
        print(self.merge_trees())
        print('Merging n trees')
        print(self.merge_n_trees([self.tree1, self.tree2]))

root_node1 = Node(50)
tree1 = Tree(root_node1)
tree1.insert(30)
tree1.insert(70)
tree1.insert(20)
tree1.insert(40)
tree1.insert(60)
tree1.insert(80)

tree1.print_in_order()
tree1.print_post_order()
tree1.print_pre_order()

root_node2 = Node(45)
tree2 = Tree(root_node2)
tree2.insert(25)
tree2.insert(65)
tree2.insert(35)
tree2.insert(55)
tree2.insert(75)

root_node3 = Node(45)
tree3 = Tree(root_node3)
tree3.insert(100)
tree3.insert(110)
tree3.insert(120)
tree3.insert(130)
tree3.insert(140)

solution = Solution(tree1, tree2)

merged_tree = solution.merge_trees()

print("In-order traversal of merged tree:")
merged_tree.print_in_order()
print(merged_tree.root.value)

merged_n_trees = solution.merge_n_trees([tree3, tree1, tree2])
print("In-order traversal of merged n trees:")
merged_n_trees.print_in_order()
