from code_challenges.breadth_first.breadth_first import Node, BinaryTree

def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


def test_create_binary_tree():
    tree = BinaryTree()
    assert tree

def test_add_to_empty_bt():
    tree = BinaryTree()
    tree.add(7)
    actual = tree.root.value
    expected = 7
    assert actual == expected

def test_breadth():
    tree = BinaryTree()
    tree.add(7)
    tree.add(8)
    tree.add(6)
    actual = BinaryTree.breadth(tree)
    expected = [7,8,6]
    assert actual == expected

def test_breadth_many():
    tree = BinaryTree()
    tree.add(7)
    tree.add(8)
    tree.add(6)
    tree.add(20)
    tree.add(43)
    tree.add(2)
    tree.add(1)
    actual = BinaryTree.breadth(tree)
    expected = [7,8,6,20,43,2,1]
    assert actual == expected

