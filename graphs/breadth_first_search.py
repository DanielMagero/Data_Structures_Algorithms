from collections import deque

def bfs(graph, start) :

  visited = set()

  queue = deque([start])
  output = []

  while queue:
    node = queue.popleft() ## get rid of first element
    if node not in visited:
      print(node, end = " ")
      visited.add(node)
      output.append(node)

      for neighbour in graph[node]:
        if neighbour not in visited:
          queue.append(neighbour)
  return output

graph = {
  "A" : ["S", "D"],
  "B" : ["S", "D"],
  "C" : ["S", "D"],
  "D" : ["A", "B", "C"],
  "S" : ["A", "B", "C"]
}

bfs(graph, "S")