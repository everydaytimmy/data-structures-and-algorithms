from code_challenges.find_maximum_binary_tree.find_maximum_binary_tree import Node, BinaryTree, BinarySearchTree

def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"

def test_create_binary_tree():
    tree = BinaryTree()
    assert tree

def test_max_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(20)
    tree.add(3)
    tree.add(45)
    tree.add(50)
    tree.add(-1)
    actual = tree.max()
    expected = 50
    assert actual == expected
