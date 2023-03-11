
from classes import QueueIterator

class Queue:

    def __init__(self):
        self.head = None

    def __str__(self):
        '''Represents the elements within the queue'''
        nodes = ", ".join(f"{node}" for node in self)
        return f"[{nodes}]"

    def __repr__(self):
        '''Represents the queue for debugging'''
        return f"{self.__class__.__name__}({self})"

    def __iter__(self):
        '''Iterate over the elements of the queue'''
        return QueueIterator(self)

    def enqueue(self, value):
        '''Adds a node to the queue'''
        node = Node(value)
        current_node = self.head
        while True:
            if self.head is None:
                self.head = node
            else:
                next_node = getattr(current_node, 'next')
                if next_node is not None:
                    current_node = current_node.next
                    continue
                else:
                    current_node.next = node
            break

    def dequeue(self):
        '''Removes the current head from the queue and returns it'''
        new_head = self.head.next
        node_value = self.head.data
        self.head = new_head
        return node_value

    def peek(self):
        '''Preview the head of the queue'''
        current_head = self.head.data
        print(f"Next element in queue: {current_head}")


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
