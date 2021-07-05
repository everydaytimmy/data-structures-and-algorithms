from code_challenges.graph.graph import Graph, Vertex

def test_add_node():
    graph = Graph()

    expected_value = 'noodle'

    actual = graph.add_node('noodle')
    assert actual.value == expected_value

def test_get_nodes():
    graph = Graph()
    graph.add_node("pizza")

    actual = graph.get_nodes()

    expected = 1

    assert len(actual) == expected
    assert isinstance(actual[0], Vertex)
    assert actual[0].value == "pizza"

def test_size_graph():
    graph = Graph()

    graph.add_node("horse")
    graph.add_node("lamb")
    actual = graph.size()
    expected = 2
    assert actual == expected


def test_get_neighbors():
    graph = Graph()
    vertex1 = graph.add_node('Chicken')
    vertex2 = graph.add_node('Egg')
    graph.add_edge(vertex1, vertex2, 5)
    neighbors = graph.get_neighbors(vertex1)
    assert len(neighbors) == 1
    single_edge = neighbors[0]
    assert single_edge.vertex.value == 'Egg'
    assert single_edge.weight == 5



def test_get_neighbors_solo():
    graph = Graph()
    spam_vertex = graph.add_node("spam")

    graph.add_edge(spam_vertex, spam_vertex)

    neighbors = graph.get_neighbors(spam_vertex)

    assert len(neighbors) == 1

    single_edge = neighbors[0]

    assert single_edge.vertex.value == "spam"
    assert single_edge.weight == 0
