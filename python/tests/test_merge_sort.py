from code_challenges.merge_sort.merge_sort import merge_sort, merge

def test_merge():
    assert merge_sort

def test_merge1():
    actual = merge_sort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_merge2():
    actual = merge_sort([3,4,12,42,-8,15])
    expected = [-8,3,4,12,15,42]
    assert actual == expected
