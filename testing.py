'''
def binarySearch(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      left = mid + 1
    else:
      right = mid -1
  return "Element not found"

array = [4,6,7,8,9,10,22]

target = 22

result  = binarySearch(array, target)
print(f"Element at index {result}")


def linearSearch(array, target):
  for i in range(len(array)):
    if array[i] == target:
      return i

array = [4,6,7,8,9,10,22]

target = 22

result = linearSearch(array, target)

print(f"{target} found at index {result}")


queue = []

def enque(value):
  queue.append(value)

def deque():
  queue.pop(0)

enque(1)
enque(2)
enque(3)
enque(4)
enque(5)


print(f"queue = ", queue)
deque()
deque()

print(f"queue = ", queue)

stack = []
def push(value):
  stack.append(value)

def pop():
  stack.pop()

push(3)
push(5)
push(2)
push(7)
push(9)

print(f"Stack =", stack)

pop()
pop()
print(f"Stack =", stack)


def factorial(n):
  if n < 0:
    return "No negatives"
  elif n == 0 or n == 1:
    return n
  else:
    return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


graph = {}

def addNode(node):
  graph[node] = []

def addEdge(node1, node2):
  graph[node1].append(node2)
  graph[node2].append(node1)

addNode("A")
addNode("B")
addNode("C")
addNode("D")
addNode("E")
addNode("F")

addEdge("A", "B")
addEdge("A", "C")
addEdge("B", "D")
addEdge("C", "E")
addEdge("D", "E")
addEdge("D", "F")

print(graph)





def addNode(node, data, next):
  node = {}
  node['data'] = []
  node['next'] = []

  node['data'].append(data)
  node['next'].append(next)
  return node

node1 = "n1"
node2 = "n2"
node3 = "n3"
node4 = "n4"
node5 = "n5"


print(addNode(node1, 3, node2))
print(addNode(node2, 15, node3))
print(addNode(node3, 6, node4))
print(addNode(node4, 8, node5))
'''


def addNode(node, leftnode, rightnode):
  return{'data': node, 'left': leftnode, 'right' : rightnode}
  
print(addNode("R", "A", "B"),
addNode("A", "C", "D"),
addNode("B", "E", "F"),
addNode("C", " ", "G"))


