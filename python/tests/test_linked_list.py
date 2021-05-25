from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList

def test_insert():
    list = LinkedList(Node("Buddy"))
    assert list.head.data == "Buddy"
    list.insert('Guy')
    list.insert('Friend')
    assert list.head.data == 'Friend'

def test_append_end():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    actual = list.head.data
    expected = "rock"
    assert actual == expected

def test_includes():
    list = LinkedList()
    list.insert('rubber')
    list.insert('baby')
    list.insert('buggy')
    list.insert('bumpers')
    actual = list.includes('baby')
    expected = True
    assert actual == expected

def test_not_includes():
    list = LinkedList()
    list.insert('rubber')
    list.insert('baby')
    list.insert('buggy')
    list.insert('bumpers')
    actual = list.includes('rad')
    expected = False
    assert actual == expected

def test_head():
    node = Node('rubber')
    actual = node.next
    expected = None
    assert actual == expected

def test_to_string():
    list = LinkedList()
    list.insert("c")
    list.insert("b")
    list.insert("a")
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

def insert_before_value():
    list = LinkedList()
    list.insert('bumpers')
    list.insert('baby')
    list.insert('rubber')
    actual = list.inject_b('bumpers', 'buggy')
    expected = ['rubber', 'baby', 'buggy', 'bumpers']
    assert actual == expected

def insert_after_value():
    list = LinkedList()
    list.insert('bumpers')
    list.insert('baby')
    list.insert('rubber')
    actual = list.inject_b('baby', 'buggy')
    expected = ['rubber', 'baby', 'buggy', 'bumpers']
    assert actual == expected


def test_x_fromend():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    list.append_item('machinegun')
    actual = list.x_fromend(2)
    expected = 'paper'
    assert actual == expected

def test_x_fromend():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    list.append_item('machinegun')
    actual = list.x_fromend(10)
    expected = 'Exception'
    assert actual == expected

def test_x_fromend():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    list.append_item('machinegun')
    actual = list.x_fromend(0)
    expected = 'machinegun'
    assert actual == expected

def test_x_fromend():
    list = LinkedList()
    list.append_item('machinegun')
    actual = list.x_fromend(0)
    expected = 'machinegun'
    assert actual == expected

def test_x_fromend():
    list = LinkedList()
    list.append_item('machinegun')
    actual = list.x_fromend(-2)
    expected = 'Exception'
    assert actual == expected

