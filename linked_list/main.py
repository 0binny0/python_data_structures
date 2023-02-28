
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
        '''Adds a node to the end of the linked list'''
        node = self.Node(data)
        current = self.head
        while True:
            if current.next is None:
                current.next = node
                return node
            current = current.next

    def insert(self, node_value, data):
        '''Inserts a node in the middle of the linked list'''
        node = self.Node(data)
        current_node = self.head
        while current_node.data != node_value:
            current_node = current_node.next
        old_next_node = current_node.next
        current_node.next = node
        node.next = old_next_node
        return node

    def delete(self, node_value):
        '''Delete a node from the linked list'''
        current_node = self.head
        while current_node is not None:
            if current_node is self.head and current_node.data == node_value:
                head = current_node.next
                self.head = head
                break
            else:
                if current_node.next.data == node_value:
                    removed_node = current_node.next
                    new_next_node = removed_node.next
                    current_node.next = new_next_node
                    break
                else:
                    current_node = current_node.next

    def iter(self):
        if self.head is None:
            raise StopIteration("No nodes exist")
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
        raise StopIteration("End of the list")


    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f"Node ({self.data})"
