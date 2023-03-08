
import sys

from funcs import prompt_list_operation, get_replaced_node, cls


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        '''A string representation of the linked list'''
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
        '''Checks for whether a node exists with the given number'''
        current_node = self.head
        while current_node is not None:
            if current_node.data == number:
                return True
            current_node = current_node.next
        return False

    def __len__(self):
        '''References the total number of nodes in the linked list'''
        total_nodes = 0
        current_node = self.head
        while current_node is not None:
            total_nodes += 1
            current_node = current_node.next
        return total_nodes

    def prepend(self, data):
        '''Sets the head of the linked list'''
        node = self.Node(data)
        if self.head is None:
            self.head = node
        else:
            next_node = self.head.next
            self.head = node
            self.head.next = next_node

    def append(self, data):
        '''Adds a node to the end of the linked list'''
        node = self.Node(data)
        current_node = self.head
        if current_node is None:
            self.head = node
        else:
            while True:
                if current_node.next is None:
                    current_node.next = node
                    return node
                current_node = current_node.next

    def insert(self, node_value, data):
        '''Inserts a node in the middle of the linked list'''
        node = self.Node(node_value)
        current_node = self.head
        if current_node.data == data:
            old_head = self.head
            new_head = node
            self.head = new_head
            self.head.next = old_head
        else:
            while current_node is not None:
                next_node = getattr(current_node, 'next')
                if next_node is not None:
                    if current_node.next.data != data:
                        current_node = current_node.next
                    else:
                        new_next_node = current_node.next
                        node.next = new_next_node
                        current_node.next = node
                        break



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


    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f"Node ({self.data})"

def main():
    linked_list = LinkedList()
    while True:
        cls()
        operation, node = prompt_list_operation(linked_list)
        if not node:
            if operation == "EXIT":
                cls()
                sys.exit()
            continue
        else:
            if operation == "SET":
                linked_list.prepend(node)
            elif operation == "APPEND":
                linked_list.append(node)
            elif operation == "DELETE":
                linked_list.delete(node)
            elif operation == "INSERT":
                replaced_node = get_replaced_node(linked_list)
                if not replaced_node:
                    continue
                linked_list.insert(node, replaced_node)


if __name__ == "__main__":
    main()
