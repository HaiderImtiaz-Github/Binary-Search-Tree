class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while temp is not None:
                if temp.value == value:
                    return False  # Value already exists in the tree
                elif value < temp.value:
                    if temp.left is None:
                        temp.left = new_node  # Assign new_node to the left child
                        return True
                    else:
                        temp = temp.left  # Move to the left child
                else:  # value > temp.value
                    if temp.right is None:
                        temp.right = new_node  # Assign new_node to the right child
                        return True
                    else:
                        temp = temp.right  # Move to the right child

    def contains(self, value):
        if self.root == None:
            return False
        else:
            temp = self.root
            while temp is not None:
                if temp.value == value:
                    return True
                elif value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
            return False