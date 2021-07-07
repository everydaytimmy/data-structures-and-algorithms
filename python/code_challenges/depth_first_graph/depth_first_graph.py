from code_challenges.graph.graph import Graph, Vertex

def depth_traversal(node, graph):
    visited = set()
    stack = Stack()
    nodes = []

    stack.push(node)

    while stack.top:
        current = stack.pop()
        nodes.append(current)
        neighbors = graph.get_neighbors(current)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.push(neighbor)
                    visited.add(neighbor)

    # breakpoint()
    return nodes



class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node (value, self.top)

    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


#### Big Brain Energy ####
# def depth_first_pre_order(first_vertex, graph):
#   visited = {}
#   collection = []
#   def walk(start_vertex):
#     nonlocal visited, collection, graph
#     if start_vertex is None:
#       return
#     if start_vertex not in visited:
#       collection.append(start_vertex)
#       visited[start_vertex] = True
#     if graph._adjacency_list.get(start_vertex):
#       for end_vertex in graph._adjacency_list.get(start_vertex):
#         walk(end_vertex)
#   walk(first_vertex)
#   return collection
