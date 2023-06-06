
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


class TestStackString(TestCase):
    '''Verify that a string can represent the elements within a Stack'''

    def setUp(self):
        stack = Stack()
        stack.head = stack.Element(1)
        stack.head.next = stack.Element(2)
        self.stack_string = str(stack)

    def test_stack_str_method(self):
        self.assertEqual(self.stack_string, "[1, 2]")


class TestStackLenMethod(TestCase):
    '''Verify that the length of a stack can be tracked.'''

    def setUp(self):
        stack = Stack()
        element_1 = stack.Element(1)
        stack.head = element_1
        self.stack_length = len(stack)

    def test_length_of_stack(self):
        self.assertEqual(self.stack_length, 1)


class TestStackPushMethod(TestCase):
    '''Verify that a new element is appended to the stack.'''

    def setUp(self):
        stack = Stack()
        stack.push(1)
        self.elements = str(stack)

    def test_new_element_added(self):
        self.assertEqual(self.elements, "[1]")


class TestEmptyStackPopMethod(TestCase):
    '''Verify that .pop() cannot be called on an empty stack'''

    def setUp(self):
        self.stack = Stack()

    def test_empty_stack_raises_error(self):
        with self.assertRaises(Exception):
            self.stack.pop()


class TestElementPoppedFromStack(TestCase):
    '''Verify that the last element from the stack is removed calling .pop()'''

    def setUp(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.popped_element = stack.pop()

    def test_element_returned(self):
        self.assertEqual(self.popped_element, 2)

if __name__ == "__main__":
    main()
