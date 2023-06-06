

class Stack:

    def __init__(self):
        self.head = None

    def __str__(self):
        elements = ", ".join([f"{element}" for element in self])
        return f"[{elements}]"

    def __len__(self):
        length = 0
        for element in self:
            length += 1
        return length

    def __iter__(self):
        return StackIterator(self)


    class Element:

        def __init__(self, data):
            self.data = data
            self.next = None


class StackIterator:

    def __init__(self, stack):
        self.element = stack.head

    def __iter__(self):
        return self

    def __next__(self):
        current_element = self.element
        if current_element is not None:
            next_element = current_element.next
            self.element = next_element
            return current_element.data
        raise StopIteration
