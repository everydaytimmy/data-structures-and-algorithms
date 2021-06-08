from code_challenges.stacks_and_queues.invalid_error import InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def walk(root):
            if not root:
                return
            if not root.left:
                root.left = Node(value)
                return
            if root.left and not root.right:
                root.right = Node(value)
                return
            walk(root.left)
            walk(root.right)
        walk(self.root)

    @staticmethod
    def breadth(tree = None):
        list = []
        queue = Queue()
        queue.enqueue(tree.root)

        if not tree:
            return []

        while queue.peek():
            node = queue.dequeue()
            list.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return list

class Queue:
    def __init__ (self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.front is None:
            self.front = self.back = QNode(value)
        else:
            self.back.next = QNode(value)

    def dequeue(self):
        if self.front is None:
            return
        ret = self.front.value
        self.front = self.front.next
        return ret

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.front:
            return self.front.value


class QNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


