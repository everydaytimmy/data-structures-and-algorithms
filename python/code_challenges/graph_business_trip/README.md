# Challenge Summary
Write a function called business trip
Arguments: graph, array of city names
Return: cost or null
Determine whether the trip is possible with direct flights, and how much it would cost.

## Whiteboard Process
![whiteboard](./CC371WB.png)

## Efficiency
BIG O:
time ---- O(L) where L is the length of the given array
space ---- O(E) where E is the maximum number of edges in the graph. worst case is O(n * (n-1))

## Solution
def business_trip(graph, arr_cities):
 if not graph.adjacency_list:
  return False, 0

 cost = 0
 for i,city in enumerate(arr_cities):
  neighbors = graph.get_neighbors(city)
  if i+1 >=len(arr_cities): # if we're at the end of the list
   return True, cost
  if arr_cities[i+1] in graph.adjacency_list[city]:
   cost += graph.adjacency_list[city].get(arr_cities[i+1])
   continue
  return False, 0
