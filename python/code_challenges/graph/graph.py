class Vertex:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self, kind='single direction'):
        self.adjacency_list = {}
        self.type= kind

    def add_node(self, value):
        vertex = Vertex(value)
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
            return vertex
        raise Exception('Node already in list')

    def get_nodes(self):
        return tuple(self.adjacency_list.keys())

    def size(self):
        if len(self.adjacency_list) == 0:
            return None

        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.adjacency_list:
            raise KeyError("End Vertex not found in graph")

        self.adjacency_list[start_vertex][end_vertex] = weight

        if self.type == 'bidirectional':
          self.adjacency_list[end_vertex][start_vertex] = weight


    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    # def add_edge(self, start_vertex, end_vertex, weight=0):
    #     edge = Edge(end_vertex, weight)
    #     self.adjacency_list[start_vertex].append(edge)

# class Edge:
#     def __init__(self, vertex, weight):
#         self.vertex = vertex
#         self.weight = weight


