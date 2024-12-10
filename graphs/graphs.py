graph = {}

#each key will represent a node
# each value will be a list that stores the neihbours or the connected nodes

def add_node(graph, node):
  if node not in graph:
    graph[node] = []

def add_edge(graph, node1, node2):
  if node1 in graph and node2 in graph:
    graph[node1].append(node2)
    graph[node2].append(node1)
  else:
    print("One or both nodes not found in the graph.")

def display_graph(graph):
  for node, edges in graph.items():
    print(f"{node}: {edges}")


add_node(graph, "A")
add_node(graph, "B")
add_node(graph, "C")
add_node(graph, "D")
add_node(graph, "S")


add_edge(graph, "A", "B")
add_edge(graph, "C", "S")
add_edge(graph, "A", "D")
add_edge(graph, "E", "B")
add_edge(graph, "A", "S")

display_graph(graph)