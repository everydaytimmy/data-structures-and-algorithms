from code_challenges.linked_list.linked_list import LinkedList, Node

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._bucket = [None] * size

    def add(self, key, value):
        index = self.hash(key)
        if not self._bucket[index]:
            self._bucket[index] = LinkedList()

        self._bucket[index].append_item([key,value])

    def get(self, key):
        index = self.hash(key)
        bucket = self._bucket[index]

        if not bucket:
            raise KeyError("Key not found", key)

        current = bucket.head

        while current:
            if current.data[0] == key:
                return current.data[1]

        raise KeyError("Key not found", key)


    def contains(self, key):
        index = self.hash(key)
        bucket = self._bucket[index]

        if bucket is None:
            return False

        current = bucket.head

        while current:
            if current.data[0] == key:
                return True
            current = current.next
        return None

    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum *= 599
        index = sum % len(self._bucket)
        return index


