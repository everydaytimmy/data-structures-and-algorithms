class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def max(self):
        def walk(root, collection):
            if not root:
                return

            collection.append(root.value)
            walk(root.left, collection)
            walk(root.right, collection)

        collected_values = []
        walk(self.root, collected_values)
        max = 0
        for i in collected_values:
            if i > max:
                max = i
        return max

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
        def walk(root, value):
            if not root:
                return False

            return (root.value == value or walk(root.left, value) or walk(root.right, value))

        return walk(self.root, value)


    def pre_order(self):
        def walk(root, collection):
            if not root:
                return

            collection.append(root.value)
            walk(root.left, collection)
            walk(root.right, collection)

        collected_values = []
        walk(self.root, collected_values)
        return collected_values


    def in_order(self):
        def walk(root, collection):
            if not root:
                return

            walk(root.left, collection)
            collection.append(root.value)
            walk(root.right, collection)

        collected_values = []
        walk(self.root, collected_values)
        return collected_values

    def post_order(self):
        def walk(root, collection):
            if not root:
                return

            walk(root.left, collection)
            walk(root.right, collection)
            collection.append(root.value)

        collected_values = []
        walk(self.root, collected_values)
        return collected_values
