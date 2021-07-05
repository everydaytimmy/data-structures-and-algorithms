# Graphs
Implementation of graph data structure

## Challenge
Create a class and functions that will allow a user to implement a grap. Functions should be able to add and get nodes, add and get edges, check the size, and determine a nodes neighbors

## Approach & Efficiency
The functions will be O(1) while space is O(N)

## API
`add_node()` - this adds a new node (vertex) to a graph. It takes in one argument (value) and returns a vertex with that value.

`get_node()` - this returns all of the nodes in
the graph. It takes no arguments and returns a tuple of all the vertices in the graph.

`add_edge()` = this add a new connection between vertices. It takes three arguments - Starting Vertex, Ending Vertex, and a Weight (default = 0) and has no retrun value.

`get_neighnors()` - this function returns the neighbors of a vertex. It takes in one argument (vertex) and returns the neighbors to it.

`size()` - this function takes not arguments and returns the length of the dictionary that represents the graph.
