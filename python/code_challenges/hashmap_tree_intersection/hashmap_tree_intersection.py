from code_challenges.tree.tree import BinarySearchTree


def tree_intersection(tree1, tree2):
    list1 = BinarySearchTree.pre_order(tree1)
    answer_key = []

    for i in list1:
        if tree2.contains(i):
            answer_key.append(i)

    return answer_key
