from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Cat, Dog,  Queue, AnimalShelter


def test_single_animal():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
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

def test_animal_dequeue_none():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue('lion')
    expected = None
    assert actual == expected
