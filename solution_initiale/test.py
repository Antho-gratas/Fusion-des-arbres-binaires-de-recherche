from typing import List
from tree.tree import Tree
from merge.merge import MergeBST

class Solution:
    def __init__(self, A1: Tree, A2: Tree, order1: str, order2: str):
        self.A1 = A1
        self.A2 = A2
        self.merge = MergeBST(A1, A2)
        self.order1 = order1
        self.order2 = order2
    
    def merge_trees(self)-> Tree:
        return self.merge.merge(self.order1, self.order2)
    
    def merge_n_trees(self, trees: List[Tree])-> Tree:
        return self.merge.merge_n_trees(trees, self.order1, self.order2)

    def run(self):
        print("A1:")
        self.A1.print_tree()
        print("A1 In-order: ")
        self.A1.print_in_order()
        print("A1 Post-order: ")
        self.A1.print_post_order()
        print("A1 Pre-order: ")
        self.A1.print_pre_order()
        print("A2:")
        self.A2.print_tree()
        A3: Tree = self.merge_trees()
        print("Fusion de A1 et de A2:")
        A3.print_tree()
        A4: Tree = Tree()
        A4.generate_random_tree(4)
        print("A4 (Arbre généré aléatoirement):")
        A4.print_tree()
        A5: Tree = self.merge_n_trees([self.A1, self.A2, A4])
        print("Fusion de A1, A2 et A4:")
        A5.print_tree()
        

        
A1 = Tree()
A1.insert(50)
A1.insert(30)
A1.insert(70)
A1.insert(20)
A1.insert(40)
A1.insert(60)
A1.insert(80)

A2 = Tree()
A2.insert(45)
A2.insert(25)
A2.insert(65)


# Test for "in-order" and "pre-order"
print('Test for "in-order" and "pre-order"')
solution = Solution(A1, A2, "in-order", "pre-order")
solution.run()

# Test for "in-order" and "post-order"
if (str(input('Continue with test for "in-order"  and "post-order" ?(y/n)')) == "y"):
    print('Test for "in-order" and "post-order"')
    solution = Solution(A1, A2, "in-order", "post-order")
    solution.run()

# Test for "pre-order" and "pre-order"    
if (str(input('Continue with test for "pre-order" and "pre-order" ?(y/n)')) == "y"):
    print('Test for "pre-order" and "pre-order"')
    solution = Solution(A1, A2, "pre-order", "pre-order")
    solution.run()


# Test for 50 000 and 20 000 nodes
if (str(input('Continue with test for trees with big number of values ? (y/n)')) == "y"):
    print('Test for 50 000 and 20 000 nodes')
    T1: Tree = Tree()
    T2: Tree = Tree()
    T1.generate_random_tree(50000)
    T2.generate_random_tree(20000)
    solution2 = Solution(T1, T2, "in-order", "post-order")
    solution2.merge_trees().print_in_order()
