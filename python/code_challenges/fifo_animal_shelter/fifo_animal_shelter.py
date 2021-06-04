from collections import deque

class Queue(deque):

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        return self.popleft()

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        return [0]

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        else:
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog" and self.dogs:
            return self.dogs.dequeue()

        if pref == "cat" and self.cats:
            return self.cats.dequeue()

        return None



class Cat:
    pass

class Dog:
    pass


