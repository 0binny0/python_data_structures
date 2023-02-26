
from unittest import TestCase, main

from main import LinkedList

class TestLinkedListHead(TestCase):
    '''Verify a new linked list has a head of None'''

    def setUp(self):
        self.linked_list = LinkedList()

    def test_linked_list_head_is_none(self):
        self.assertIsNone(self.linked_list.head, None)
        

if __name__ == "__main__":
    main()
