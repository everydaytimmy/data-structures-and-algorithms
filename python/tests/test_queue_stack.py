from code_challenges.queueWithStacks.queueWithStacks import Stack, Node

def test_is_stack():
    assert Stack()

def test_pop():
    stack = Stack()
    stack.enqueue('Dwight')
    stack.enqueue('Michael')
    stack.enqueue('Pam')
    stack.enqueue('Jim')
    stack.enqueue('Andy')
    stack.dequeue()
    actual = stack.top.value
    expected = 'Michael'
    assert actual == expected

def test_pop1():
    stack = Stack()
    stack.enqueue('Dwight')
    stack.enqueue('Michael')
    stack.enqueue('Pam')
    stack.enqueue('Jim')
    stack.enqueue('Andy')
    stack.enqueue('Creed')
    stack.dequeue()
    actual = stack.top.value
    expected = 'Michael'
    assert actual == expected


def test_push():
    stack = Stack()
    stack.enqueue('Dwight')
    actual = stack.top.value
    expected = 'Dwight'
    assert actual == expected
