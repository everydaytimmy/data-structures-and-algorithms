class Stack:
    def __init__(self):
        self.top = None

    def enqueue(self, value):
        self.top = Node (value, self.top)

    def reverse(self):
        prev = None
        current = self.top
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.top = prev

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
