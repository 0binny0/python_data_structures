
from unittest import TestCase, main
from unittest.mock import patch

from main import LinkedList

class TestLinkedListHead(TestCase):
    '''Verify a new linked list has a head of None'''

    def setUp(self):
        self.linked_list = LinkedList()

    def test_linked_list_head_is_none(self):
        self.assertIsNone(self.linked_list.head, None)


class TestPrependNodeToLinkedList(TestCase):

    def setUp(self):
        self.initial_head = LinkedList.Node(1)
        linked_list = LinkedList()
        linked_list.head = self.initial_head
        self.updated_head = linked_list.prepend(2)

    def test_prepend_sets_new_head(self):
        self.assertEqual(self.updated_head.data, 2)
        self.assertEqual(self.updated_head.next.data, 1)


class TestAppendNodeToLinkedList(TestCase):


    def setUp(self):
        self.linked_list = LinkedList()
        self.mock_head_config = {
            "data": 1
        }

    def test_appended_node(self):
        with patch.object(self.linked_list, 'head', **self.mock_head_config) as mock_head:
            mock_head.next = None
            node = self.linked_list.append(2)
            self.assertEqual(self.linked_list.head.data, 1)
            self.assertEqual(self.linked_list.head.next.data, 2)
            self.assertIsNone(self.linked_list.head.next.next)



if __name__ == "__main__":
    main()
