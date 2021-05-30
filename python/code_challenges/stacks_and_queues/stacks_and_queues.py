from code_challenges.stacks_and_queues.invalid_error import InvalidOperationError


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node (value, self.top)

    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top.value

class Queue:
    def __init__ (self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.rear = Node(value)
            self.front = self.rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        old_front = self.front
        self.front = self.front.next
        old_front.next = None

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.rear:
            return self.rear.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
