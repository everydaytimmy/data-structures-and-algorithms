class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        self.head = Node(data, self.head)

    def append_item(self, data):
        new_node = Node(data)
        current = self.head

        if not self.head:
            self.head = new_node
            return

        while current.next:
            current = current.next

        current.next = new_node

    def includes(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def find_all(self):
        values = []
        current = self.head

        while current:
            values.append(current.data)
            current = current.next

        return values

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += "{ " + current.data + " } -> "
            current = current.next
        string += 'None'
        return string

    def inject_b(self, index, value):
        current = self.head
        while current:
            if current.next.value != index:
                current = current.next
            else:
                old_next = current.next
                current.next = Node(value, old_next)
                break

    def inject_a(self, index, value):
        current = self.head
        while current:
            if current.data == index:
                current.next = Node(value, current.next)
                break
            else:
                current = current.next



class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
