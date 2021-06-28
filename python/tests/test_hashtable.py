from code_challenges.hashtable.hashtable import Hashtable


def text_exists()  :
    assert Hashtable

def test_add():
    ht = Hashtable()
    actual = ht.add('rum ham', 11)
    expected = None
    assert actual == expected

def test_get_value():
    ht = Hashtable()
    ht.add('rum ham', 6)
    actual = ht.get('rum ham')
    expected = 6
    assert actual == expected

def test_hash():
    ht = Hashtable()
    actual = ht.hash('rum ham')
    assert 0 <= actual <= 1024

def test_contains():
    ht = Hashtable()
    ht.add('rum ham', 6)
    actual = ht.contains('toe knife')
    expected = False
    assert actual == expected


# def test_collision():
#     ht = Hashtable()
#     ht.add('rum ham', 6)
#     ht.add('toe knife', 6)
#     one = ht.get('rum ham')
#     two = ht.get('toe knife')
#     assert one != two
