from typing import List
from tree.tree import Tree
from merge.merge import MergeBST

'''class Solution:
    def __init__(self, tree1: Tree, tree2: Tree):
        self.tree1 = tree1
        self.tree2 = tree2
        self.merge = MergeBST(tree1, tree2)
    
    def merge_trees(self)-> Tree:
        return self.merge.merge()
    
    def merge_n_trees(self, trees: List[Tree])-> Tree:
        return self.merge.merge_n_trees(trees)

    def run(self):
        print('Merging two trees')
        print(self.merge_trees())
        print('Merging n trees')
        print(self.merge_n_trees([self.tree1, self.tree2]))
'''


tree = Tree()
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80) # Générer un arbre de 10 valeurs
tree.print_in_order() 