class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self, level=0):
        print('  ' * level + self.data)
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)

# Creating the tree
root = Node('root')
root.left = Node('left')
root.right = Node('right')

# Adding more nodes
root.left.left = Node('left.left')
root.left.right = Node('left.right')

# Printing the tree
root.print_tree()
