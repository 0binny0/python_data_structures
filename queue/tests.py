
from unittest import TestCase, main
from unittest.mock import patch

from main import Queue
from funcs import get_queue_element


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


class TestSeekOperation(TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)

    def test_queue_preview_head(self):
        with patch("main.print", return_value="Next element in queue: 1") as mock_print:
            self.queue.peek()
            self.assertTrue(mock_print.called)


class GenerateNewElementForQueueDisallowed(TestCase):
    '''Verify that an attempt to add a duplicate item into
    the queue results in no action performed.'''

    @patch("funcs.print", return_value="Invalid selection made.")
    @patch("funcs.input", return_value="E")
    def setUp(self, mock_input, mock_print):
        queue = Queue()
        queue.enqueue("A")
        queue.enqueue("E")
        self.value = get_queue_element(queue)

    def test_element_provided_for_queue(self):
        self.assertIsNone(self.value)


class GenerateNewElementForQueueAllowed(TestCase):
    '''Verify that an attempt to add a duplicate item into
    the queue results in no action performed.'''

    @patch("funcs.input", return_value="E")
    def setUp(self, mock_input):
        queue = Queue()
        queue.enqueue("A")
        self.value = get_queue_element(queue)

    def test_element_provided_for_queue(self):
        self.assertEqual(self.value, 'E')


if __name__ == "__main__":
    main()
