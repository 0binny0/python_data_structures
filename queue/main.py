
class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, value):
        node = Node(value)
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
        if current_node is self.head:
            self.head = node
        else:
            current_node = node


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
