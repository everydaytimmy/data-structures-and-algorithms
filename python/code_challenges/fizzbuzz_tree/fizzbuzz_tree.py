
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Ktree():
    def __init__(self):
        self.root = None

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

def fizz_buzz(tree):

    queue = Queue()
    queue.enqueue(tree.root)
    new_tree = KTree()

    while queue.peek():
        node = queue.dequeue()
        new_value = fizzify(node)
        new_node = Node(new_value)
        for child in node.children:
            queue.enqueue(child)



def fizzify(value):
    if value % 3 == 0 or value % 5 == 0:
        return "fizzbuzz"
    if value % 3 == 0:
        return "fizz"
    if value % 5 == 0:
        return "buzz"
    else:
        return str(value)

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
