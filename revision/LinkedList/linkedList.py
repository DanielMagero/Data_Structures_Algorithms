class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")


node1 = {'data': 3, 'next': None}
node2 = {'data': 5, 'next': None}
node3 = {'data': 13, 'next': None}
node4 = {'data': 2, 'next': None}

# Link the nodes
node1['next'] = node2
node2['next'] = node3
node3['next'] = node4

# Traverse the linked list
currentNode = node1
while currentNode:
    print(currentNode['data'], end=" -> ")
    currentNode = currentNode['next']
print("null")