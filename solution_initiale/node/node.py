class Node:
    '''Node class for binary search tree'''

    def __init__(self, value: int) -> None:
        self.value = value  
        self.left = None    # The left node
        self.right = None   # The right node
