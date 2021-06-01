import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Stack, Queue, Node
from code_challenges.stacks_and_queues.invalid_error import InvalidOperationError


def test_is_stack():
    assert Stack()

def test_push():
    stack = Stack()
    stack.push('Dwight')
    actual = stack.top.value
    expected = 'Dwight'
    assert actual == expected

def test_push_many():
    stack = Stack()
    stack.push('Dwight')
    stack.push('Michael')
    stack.push('Jim')
    actual = stack.top.value
    expected = 'Jim'
    assert actual == expected

def test_pop():
    stack = Stack()
    stack.push('Dwight')
    stack.push('Michael')
    stack.push('Jim')
    stack.pop()
    actual = stack.top.value
    expected = 'Michael'
    assert actual == expected

def test_pop_till_empty():
    stack = Stack()
    stack.push('Dwight')
    stack.push('Michael')
    stack.push('Jim')
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek():
    stack = Stack()
    stack.push('Dwight')
    stack.push('Michael')
    stack.push('Jim')
    stack.push('Andy')
    stack.peek()
    actual = stack.top.next.value
    expected = 'Jim'
    assert actual == expected

def test_peek():
    stack = Stack()
    stack.push('Dwight')
    stack.push('Michael')
    stack.push('Jim')
    stack.push('Andy')
    stack.peek()
    actual = stack.top.value
    expected = 'Andy'
    assert actual == expected

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty()

def test_pop_on_empty():
    new_stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        new_stack.pop()

    assert str(e.value) == "Method not allowed on empty collection"

def test_peek_on_empty():
    new_stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        new_stack.peek()

def test_enqueue():
    queue = Queue()
    queue.enqueue('Ron')
    actual = queue.rear.value
    expected = 'Ron'
    assert actual == expected

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue('Ron')
    queue.enqueue('Andy')
    queue.enqueue('Leslie')
    actual = queue.rear.value
    expected = 'Leslie'
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue('Dennis')
    queue.enqueue('Mac')
    queue.enqueue('Charlie')
    queue.enqueue('Dee')
    queue.dequeue()
    actual = queue.front.value
    expected = 'Mac'
    assert actual == expected

def test_dequeue_empty():
    queue = Queue()
    queue.enqueue('Dennis')
    queue.enqueue('Mac')
    queue.enqueue('Charlie')
    queue.enqueue('Dee')
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_new_queue():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_call_dequeue_on_empty_queue():
    new_queue = Queue()
    with pytest.raises(InvalidOperationError) as e:
        new_queue.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"

def test_peek_on_empty_queue():
    new_queue = Queue()
    with pytest.raises(InvalidOperationError) as e:
        new_queue.peek()

    assert str(e.value) == "Method not allowed on empty collection"

# Write tests to prove the following functionality:

# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception
