from code_challenges.graph.graph import Graph, Vertex


def business_trip(graph, arr_cities):
  if not graph.adjacency_list:
    return False, 0

  cost = 0
  for i,city in enumerate(arr_cities):
    neighbors = graph.get_neighbors(city)
    if i+1 >=len(arr_cities):
      return True, cost
    if arr_cities[i+1] in neighbors:
      cost += graph.adjacency_list[city].get(arr_cities[i+1])
      continue
    return False, 0

