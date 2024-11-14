class NodeAVL:
    '''Node class for AVL binary search tree'''
    
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: NodeAVL = None
        self.right: NodeAVL = None
        self.parent: NodeAVL = None 
        self.height: int = 1
        
    def update_height(self) -> None:
        '''
        Update the height of the node based on its children's heights.
        Returns:
            None
        '''
        if self.left is not None :
            left_height: int = self.left.get_height()  
        else:
            left_height: int = 0
        if self.right is not None :
            right_height: int = self.right.get_height()  
        else: 
            right_height: int = 0
        self.height = max(left_height, right_height) + 1

    def get_height(self) -> int:
        '''
        Get the height of a node.
        Returns:
            int: Height of the node.
        '''
        return self.height
