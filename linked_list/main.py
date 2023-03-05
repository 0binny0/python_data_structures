
class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = ""
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                nodes += f"[{current_node.data}]"
            else:
                nodes += f"[{current_node.data}] - "
            current_node = current_node.next
        return nodes

    def __contains__(self, number):
        current_node = self.head
        while current_node is not None:
            if current_node.data == number:
                return True
            current_node = current_node.next
        return False

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
            raise StopIteration
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
        return


    def __len__(self):
        total_nodes = 0
        current_node = self.head
        while current_node is not None:
            total_nodes += 1
            current_node = current_node.next
        return total_nodes


    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f"Node ({self.data})"

def main():
    linked_list = LinkedList()
    while True:
        operation, node = get_list_operation(linked_list)
        if not node:
            continue
        else:
            if operation == "SET":
                linked_list.prepend(node)
            elif operation == "APPEND":
                linked_list.append(node)
            elif operation == "DELETE":
                linked_list.remove(node)
            elif operation == "INSERT":
                # replaced_node = get_replaced_node(linked_list)
                linked_list.insert(node, replaced_node)
            else:
                sys.exit()
