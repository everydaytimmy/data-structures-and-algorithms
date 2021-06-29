from code_challenges.hashmap_tree_intersection.hashmap_tree_intersection import tree_intersection
from code_challenges.tree.tree import Node, BinaryTree, BinarySearchTree


def test__tree_compare():
    tree1 = BinarySearchTree()
    tree1.add(5)
    tree1.add(2)
    tree1.add(3)
    tree2 = BinarySearchTree()
    tree2.add(5)
    tree2.add(1)
    tree2.add(4)
    actual = tree_intersection(tree1, tree2)
    expected = [5]
    assert actual == expected

def test_tree_compare_one():
    tree1 = BinarySearchTree()
    tree1.add(5)
    tree1.add(2)
    tree1.add(3)
    tree2 = BinarySearchTree()
    tree2.add(5)
    tree2.add(1)
    tree2.add(4)
    actual = tree_intersection(tree1, tree2)
    expected = [5]
    assert actual == expected

def test_tree_compare_two():
    tree1 = BinarySearchTree()
    tree1.add(5)
    tree1.add(2)
    tree1.add(3)
    tree1.add(2)
    tree1.add(1)
    tree1.add(2)
    tree1.add(4)
    tree2 = BinarySearchTree()
    tree2.add(5)
    tree2.add(1)
    tree2.add(4)
    actual = tree_intersection(tree1, tree2)
    expected = [5, 1, 4]
    assert actual == expected

def test_tree_compare_three():
    tree1 = BinarySearchTree()
    tree1.add(5)
    tree1.add(2)
    tree1.add(3)
    tree1.add(2)
    tree1.add(1)
    tree1.add(2)
    tree1.add(4)
    tree2 = BinarySearchTree()
    tree2.add(12)
    tree2.add(22)
    tree2.add(24)
    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected
