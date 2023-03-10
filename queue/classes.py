
class QueueIterator:

    def __init__(self, obj):
        self.node = obj.head

    def __iter__(self):
        return self

    def __next__(self):
        next_node = getattr(self.node, 'next', None)
        if self.node is not None:
            current_node = self.node
            self.node = next_node
            return current_node.data
        raise StopIteration
