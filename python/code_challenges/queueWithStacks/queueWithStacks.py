class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node (value, self.top)

    def pop(self):
        value = self.top.value
        self.top = self.top.next
        return value

    def enqueue(self, value):
        self.top = Node (value, self.top)

    def dequeue(self):
        prev = None
        current = self.top
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.top = prev
        value = self.top.value
        self.top = self.top.next

        return value


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
