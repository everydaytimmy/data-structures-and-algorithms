from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Cat, Dog,  Queue, AnimalShelter

def test_is_queue():
    assert Queue()

def test_enqueue_multiple_animals():
    queue = Queue()
    queue.enqueue('Cat')
    queue.enqueue('Cat')
    queue.enqueue('Dog')
    queue.enqueue('Cat')
    actual = queue.rear.value
    expected = 'Cat'
    assert actual == expected

def test_animal_dequeue():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    shelter.enqueue(dog)
    actual = shelter.dequeue('dog')
    expected = dog
    assert actual == expected
