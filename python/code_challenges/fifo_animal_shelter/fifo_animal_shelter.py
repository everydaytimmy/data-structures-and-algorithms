from code_challenges.stacks_and_queues.invalid_error import InvalidOperationError

class AnimalShelter:
    def __init__(self):
        self.shelter = Queue()

    def enqueue(self, animal):
        self.shelter.enqueue(animal)

    def dequeue(self, animal):
        self.shelter.dequeue(animal)


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.rear = Node(value)
            self.front = self.rear

    def dequeue(self, animal):
        if not self.front:
            raise InvalidOperationError("Method not allow on empty collection")
        current = self.front
        if animal == current.value:
            old_front = self.front
            self.front = self.front.next
            old_front.next = None
            return old_front

        while animal != current.value:
            lookback = current
            current = current.next

        lookback.next = current.next
        current = None
        return current.value

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Cat:
    def __init__(self, value = 'cat'):
        self.value = value

class Dog:
    def __init__(self, value = 'dog'):
        self.value = value


