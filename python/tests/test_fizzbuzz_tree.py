from code_challenges.fizzbuzz_tree.fizzbuzz_tree import Ktree, Node, fizz_buzz

def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


def test_create_k_tree():
    tree = KTree()
    assert tree

def test_fizz_buzz():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)

    one.children = [two,five]
    two.children = [three, four]
    five.children = [six, seven, eight]
    kt = Ktree()
    kt.root = one
    actual = fizz_buzz(kt)
    expected = kt.breadth(kt)
    assert actual == expected


