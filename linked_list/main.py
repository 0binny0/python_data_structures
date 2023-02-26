
class LinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        '''Sets the head of the linked list'''
        node = self.Node(data)
        if self.head is None:
            self.head = node
        else:
            old_head = self.head
            node.next = old_head
            self.head = node
        return self.head

    def append(self, data):
        node = self.Node(data)
        current = self.head
        while True:
            if current.next is None:
                current.next = node
                return node
            current = current.next



    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f"Node ({self.data})"
