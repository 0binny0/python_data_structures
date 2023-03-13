
import sys
from time import sleep

from classes import QueueIterator
from funcs import cls, get_queue_operation, get_queue_element

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
        if self.head is None:
            print("\nQueue is empty.")
            sleep(1.5)
        else:
            new_head = self.head.next
            node_value = self.head.data
            self.head = new_head
            print(f"{node_value} is removed from the queue.")
            return node_value

    def peek(self):
        '''Preview the head of the queue'''
        if self.head is None:
            current_head = "Empty"
        else:
            current_head = self.head.data
        print(f"Next element in queue: {current_head}")
        sleep(1.5)
        return


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def main(queue):
    while True:
        while True:
            execute = get_queue_operation(queue)
            if not execute:
                continue
            else:
                break
        if execute == "EXIT":
            break
        else:
            if execute == "ADD":
                element = get_queue_element(queue)
                if not element:
                    continue
                queue.enqueue(element)
            elif execute == "PEEK":
                queue.peek()
            else:
                popped_element = queue.dequeue()
                cls()
            continue
    cls()
    sys.exit()


if __name__ == "__main__":
    queue = Queue()
    main(queue)
