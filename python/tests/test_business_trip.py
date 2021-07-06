from code_challenges.graph_business_trip.graph_business_trip import business_trip
from code_challenges.graph.graph import Graph, Vertex

def test_business_one():
    graph = Graph('bidirectional')
    boston = graph.add_node('Boston')
    seattle = graph.add_node('Seattl')
    la = graph.add_node('LA')
    sf = graph.add_node('SF')
    chi = graph.add_node('CHI')
    ny = graph.add_node('NY')
    graph.add_edge(boston, ny, 82)
    graph.add_edge(boston, chi, 90)
    graph.add_edge(ny, chi, 42)
    graph.add_edge(ny, seattle, 200)
    graph.add_edge(ny, la, 225)
    graph.add_edge(ny, sf, 230)
    graph.add_edge(chi, seattle, 175)
    graph.add_edge(seattle, sf, 85)
    graph.add_edge(sf, la, 85)
    cities = [boston, ny,la]
    actual = business_trip(graph, cities)
    expected = (True, 307)
    assert actual == expected

def test_business_two():
    graph = Graph('bidirectional')
    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, monstroplolis, 42)
    graph.add_edge(metroville, monstroplolis, 105)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, narnia, 250)
    graph.add_edge(monstroplolis, naboo, 73)
    cities = [narnia, arendelle, naboo]
    actual = business_trip(graph, cities)
    expected = (False, 0)
    assert actual == expected
