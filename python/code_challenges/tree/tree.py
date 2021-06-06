class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

class BinarySearchTree(BinaryTree):
    def add(self, value):

        node = Node(value)

        def walk(root, new_node):
            if not root:
                return

            new_value = new_node.value

            if new_value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node

            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

        if not self.root:
            self.root = node
            return

        walk(self.root, node)

    def contains(self, value):
        pass



