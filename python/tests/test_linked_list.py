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

def test_values():
    list = LinkedList()
    list.insert('bumpers')
    list.insert('buggy')
    list.insert('baby')
    list.insert('rubber')
    actual = list.find_all()
    expected = ['rubber', 'baby', 'buggy', 'bumpers']
    assert actual == expected

def test_add_before_value():
    list = LinkedList()
    list.insert('bumpers')
    list.insert('buggy')
    list.insert('rubber')
    list.inject_b('buggy', 'baby')
    actual = list.find_all()
    expected = ['rubber', 'baby', 'buggy', 'bumpers']
    assert actual == expected

def test_add_after_value():
    list = LinkedList()
    list.insert('bumpers')
    list.insert('baby')
    list.insert('rubber')
    list.inject_a('baby', 'buggy')
    actual = list.find_all()
    expected = ['rubber', 'baby', 'buggy', 'bumpers']
    assert actual == expected

def test_add_after_value1():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    list.append_item('machinegun')
    list.inject_a('scissors', 'cannon')
    actual = list.find_all()
    expected = ['rock', 'paper', 'scissors', 'cannon', 'machinegun']
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

def test_x_fromend10():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    list.append_item('machinegun')
    actual = list.x_fromend(10)
    expected = 'Exception'
    assert actual == expected

def test_x_fromend0():
    list = LinkedList()
    list.append_item('rock')
    list.append_item('paper')
    list.append_item('scissors')
    list.append_item('machinegun')
    actual = list.x_fromend(0)
    expected = 'machinegun'
    assert actual == expected

def test_x_fromend_one_item():
    list = LinkedList()
    list.append_item('machinegun')
    actual = list.x_fromend(0)
    expected = 'machinegun'
    assert actual == expected

def test_x_fromend_neg():
    list = LinkedList()
    list.append_item('machinegun')
    actual = list.x_fromend(-2)
    expected = 'Exception'
    assert actual == expected

def test_zip():
    lista = LinkedList()
    listb = LinkedList()
    lista.append_item('A')
    lista.append_item('B')
    listb.append_item('1')
    listb.append_item('2')
    answer = lista.zip_list(listb)
    actual = answer.find_all()
    expected = ['A', '1', 'B', '2']
    assert actual == expected

