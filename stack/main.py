
from classes import Stack


def main():
    stack = Stack()
    print("")
    for letter in ['A', 'B', 'C', 'D']:
        print(f"Adding {letter} to stack.")
        stack.push(letter)

    print(f"\nThe length of the stack is {len(stack)}:")
    print(f"Stack: {stack}")

    last_element_in_stack = stack.pop()

    print(f"\nCalling .pop() removes the last element in the stack: {last_element_in_stack}.")
    print(f"\nThe length of the stack is now {len(stack)}:")
    print(f"Stack: {stack}")

    for i in range(3):
        popped_element = stack.pop()
        print(f"\nRemoved {popped_element} from the stack...{stack}")

    try:
        last_element_in_stack = stack.pop()
    except Exception as e:
        print("Cannot remove anymore elements from the stack!")
    finally:
        pass

if __name__ == "__main__":
    main()
