from code_challenges.quick_sort.quick_sort import partition, quick_sort

def test_quick():
    assert quick_sort


def test_quick_sort():
    array = [ 10, 7, 8, 9, 1, 5 ]
    actual = quick_sort(0, len(array) - 1, array)
    expected = [1,5,7,8,9,10]
    assert actual == expected

def test_quick1():
    array = [8,4,23,42,16,15]
    actual = quick_sort(0, len(array) - 1, array)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_quick2():
    array = [3,4,12,42,-8,15]
    actual = quick_sort(0, len(array) - 1, array)
    expected = [-8,3,4,12,15,42]
    assert actual == expected

