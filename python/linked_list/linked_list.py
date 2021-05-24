class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False


    def find_all(self):
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string.join(current.value)
            current = current.next

        return string

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
