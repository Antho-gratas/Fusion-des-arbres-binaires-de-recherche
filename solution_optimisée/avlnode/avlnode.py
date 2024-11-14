class NodeAVL:
    '''Node class for AVL binary search tree'''
    
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None 
