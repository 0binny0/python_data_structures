
from unittest import TestCase, main

from main import Queue


class TestEnqueueOperation(TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)

    def test_head_node_value(self):
        self.assertEqual(self.queue.head.data, 1)
        self.assertIsNone(self.queue.head.next)


class TestDequeueOperation(TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.value = self.queue.dequeue()
        self.queue_head = self.queue.head

    def test_node_returned_from_dequeing(self):
        self.assertEqual(self.value, 1)
        self.assertEqual(self.queue_head.data, 2)
        self.assertIsNone(self.queue.head.next)

if __name__ == "__main__":
    main()
