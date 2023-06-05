
from unittest import TestCase, main

from classes import Stack, StackIterator

class TestStackIterator(TestCase):
    '''Verify that a Stack can be iterated over returning each element'''

    def setUp(self):
        stack = Stack()
        stack.head = stack.Element(1)
        stack.head.next = stack.Element(2)
        self.iterator = iter(StackIterator(stack))
        self.element_0 = next(self.iterator)
        self.element_1 = next(self.iterator)

    def test_stack_elements_as_string(self):
        self.assertEqual(self.element_0, 1)
        self.assertEqual(self.element_1, 2)
        with self.assertRaises(StopIteration):
            next(self.iterator)


if __name__ == "__main__":
    main()
