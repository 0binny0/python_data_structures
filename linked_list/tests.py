
from unittest import TestCase, main
from unittest.mock import patch, Mock

from main import LinkedList
from funcs import get_node_value

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
        self.assertEqual(self.n1, 1)
        self.assertEqual(self.n2, 2)
        self.assertEqual(self.n3, 3)


class TestLengthofLinkedList(TestCase):
    '''Verify that the length of the linked list
    is returned with __len__'''

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.head = LinkedList.Node(1)
        self.linked_list.head.next = LinkedList.Node(2)

    def test_len_method_(self):
        self.assertEqual(len(self.linked_list), 2)


class TestLinkedListNodesString(TestCase):
    '''Verify that nodes of the linked list are returned.'''

    def setUp(self):
        linked_list = LinkedList()
        linked_list.head = LinkedList.Node(1)
        node2 = linked_list.Node(2)
        node2.next = None
        linked_list.head.next = node2
        self.nodes = str(linked_list)

    def test_total_nodes(self):
        self.assertEqual(self.nodes, "[1] - [2]")


class TestCheckedStoredNodes(TestCase):
    '''Verify that a node can be checked for with
    "in" membership.'''

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.head = LinkedList.Node(1)
        self.node2 = LinkedList.Node(8)
        self.node2.next = None
        self.linked_list.head.next = self.node2

    def test_node_in_linked_list(self):
        self.assertIn(self.node2.data, self.linked_list)


class TestGetNodeValue(TestCase):
    '''Verify that a value for a linked list can be accepted.'''

    def setUp(self):
        linked_list = LinkedList()
        node1 = LinkedList.Node(7)
        node2 = LinkedList.Node(4)
        node1.next = node2
        linked_list.head = node1

        with patch("funcs.input", side_effect=['7',]) as mock_input:
            self.value = get_node_value(linked_list)
            self.mock = mock_input

    def test_value_submitted_for_linked_list(self):
        self.assertTrue(self.mock.called)
        self.assertEqual(self.mock.call_count, 1)




if __name__ == "__main__":
    main()
