class Node:
    '''Node class for binary search tree'''
    
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node = None
        self.right: Node = None
