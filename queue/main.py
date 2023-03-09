
class Queue:

    def __init__(self):
        self.head = None

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
<<<<<<< HEAD
        '''Preview the head of the queue'''
=======
>>>>>>> d8ec971f58ba2aeef0eb7a8a1d57f17cbc84d02b
        current_head = self.head.data
        print(f"Next element in queue: {current_head}")


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
