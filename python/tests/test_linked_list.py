from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


def test_insert():
    list = LinkedList(Node("Yo"))
    assert list.head.value == "Yo"
    list.insert('sup')
    assert list.head.value == 'sup'

def test_includes():
    list = LinkedList()
    list.insert('rubber')
    list.insert('baby')
    list.insert('buggy')
    list.insert('bumpers')
    actual = list.includes('baby')
    expected = True
    actual == expected

def test_head():
    node = Node('rubber')
    actual = node.next
    expected = None
    assert actual == expected

def test_to_string():
    list = LinkedList()
    list.insert("{ c } ->")
    list.insert("{ b } ->")
    list.insert("{ a } ->")
    actual = list.__str__()
    expected = "{ a } -> { b } -> { c } -> None"
    assert actual == expected

def test_all_values():
    list = LinkedList()
    list.insert('bumpers')
    list.insert('buggy')
    list.insert('baby')
    list.insert('rubber')
    actual = list.find_all()
    expected = ['rubber', 'baby', 'buggy', 'bumpers']
    assert actual == expected



