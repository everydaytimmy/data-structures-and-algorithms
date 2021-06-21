from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_one():
    list = [1,6,3,8,66,23,]
    actual = [1,3,6,8,23,66]
    expected = insertion_sort(list)
    assert actual == expected

def test_insertion_sorting1():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_insertion_sorting2():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_insertion_sorting3():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
