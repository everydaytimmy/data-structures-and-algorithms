from code_challenges.hashmap_left_join.hashmap_left_join import hashmap_left_join
from code_challenges.hashtable.hashtable import Hashtable

def test_exists():
    assert hashmap_left_join

def test_left_join():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('happy', 'follow')
    actual = hashmap_left_join(ht1, ht2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', None]
    ]
    for entry in expected:
        assert entry in actual

def test_left_join_one_empty():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    actual = hashmap_left_join(ht1, ht2)
    expected = [
        ['fond', 'enamored', None],
        ['wrath', 'anger', None],
    ]
    for entry in expected:
        assert entry in actual

def test_left_join_both_empty():
    ht1 = Hashtable()
    ht2 = Hashtable()
    actual = hashmap_left_join(ht1, ht2)
    expected = []
    assert actual == expected
