def dfs_stack(graph, start):
  visited = set()

  stack = [start]

  while stack:
    node = stack.pop()
    if node not in visited:
      print(node, end = " ")
      visited.add(node)

      for neighbour in reversed(graph[node]):
        if neighbour not in visited:
          stack.append(neighbour)


graph = {
  "A" : ["S", "D"],
  "B" : ["S", "D"],
  "C" : ["S", "D"],
  "D" : ["A", "B", "C"],
  "S" : ["A", "B", "C"]
}

dfs_stack(graph, "S")