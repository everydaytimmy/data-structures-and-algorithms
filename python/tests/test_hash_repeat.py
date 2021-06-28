from code_challenges.hashmap_repeated.hashmap_repeated import word_repeat
from code_challenges.hashtable.hashtable import Hashtable

def test_word_repeat():
    assert word_repeat

def test_string():
    actual = word_repeat("Once upon a time, there was a brave princess who...")
    expected = 'a'
    assert actual == expected

def test_string_1():
    actual = word_repeat("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = 'it'
    assert actual == expected

def test_string_2():
    actual = word_repeat("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected = 'summer'
    assert actual == expected
