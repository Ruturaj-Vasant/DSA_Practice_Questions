class Node:
    def __init__(self, data):
        self. data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

current = node1

while current:
    print(current.data, end="->")
    current = current.next

print('null')

new_node = Node(5)
new_node.next = node1
node1 = new_node

current = node1

while current:
    print(current.data, end="->")
    current = current.next

print('null')

node1 = node1.next

current = node1

while current:
    print(current.data, end="->")
    current = current.next

print('null')

print (f"node1: {id(node1)}, data: {node1.data}, next: {id(node1.next)}")
