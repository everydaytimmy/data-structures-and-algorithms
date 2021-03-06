class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                    yield current.value
                    current= current.next
            return value_generator()

    def __str__(self):
        out = ""

        for value in self:
            out += f"[ {value} ] ->"

        return out + "None"

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other)

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
            if current.next.data == index:
                old_next = current.next
                current.next = Node(value, old_next)
                break
            current = current.next

    def inject_a(self, index, value):
        current = self.head
        while current:
            if current.data == index:
                current.next = Node(value, current.next)
                break
            else:
                current = current.next

    def x_fromend(self, index):
        temp = []
        current = self.head
        while current:
            temp.append(current.data)
            current = current.next
        temp[::-1]
        if index > len(temp):
            return 'Exception'
        if index < 0:
            return 'Exception'
        return temp[index-1]

    def zip_list(lista,listb):
        current_a = lista.head
        current_b = listb.head
        while current_a and current_b:
            old_next_a = current_a.next
            old_next_b = current_b.next

            current_a.next = current_b

            if current_a != None:
                current_b.next = old_next_a

                current_a = old_next_a
                current_b = old_next_b
            else:
                break
        return lista



class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

        try:
            current = self.head
            for _ in range(1, self.length-num):
                current = current.next
            return current.value
        except: print('Something went wrong, please try again')
