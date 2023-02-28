
from unittest import TestCase, main
from unittest.mock import patch, Mock

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
            "data": 1,
            'next': None
        }

    def test_appended_node(self):
        with patch.object(self.linked_list, 'head', **self.mock_head_config) as mock_head:
            node = self.linked_list.append(2)
            self.assertEqual(self.linked_list.head.data, 1)
            self.assertEqual(self.linked_list.head.next.data, 2)
            self.assertIsNone(self.linked_list.head.next.next)


class TestInsertNodeToLinkedList(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        node2 = LinkedList.Node(2)
        head = LinkedList.Node(1)
        head.next = node2
        self.linked_list.head = head
        self.linked_list.insert(1, 3)

    def test_node_inserted_between_existing_nodes(self):
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.head.next.data, 3)
        self.assertEqual(self.linked_list.head.next.next.data, 2)


class TestDeleteNodeFromLinkedList(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.head = LinkedList.Node(1)
        self.linked_list.head.next = LinkedList.Node(2)
        self.linked_list.head.next.next = LinkedList.Node(3)
        self.linked_list.delete(2)

    def test_search_for_node_and_delete(self):
        self.assertEqual(self.linked_list.head.next.data, 3)


class TestLinkedListIteration(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        node3 = LinkedList.Node(3)
        node2 = LinkedList.Node(2)
        head = LinkedList.Node(1)
        self.linked_list.head = head
        self.linked_list.head.next = node2
        self.linked_list.head.next.next = node3
        generator = self.linked_list.iter()
        self.n1 = next(generator)
        self.n2 = next(generator)
        self.n3 = next(generator)

    def test_linked_list_looping(self):
        self.assertEqual(self.n1.data, 1)
        self.assertEqual(self.n2.data, 2)
        self.assertEqual(self.n3.data, 3)

if __name__ == "__main__":
    main()
