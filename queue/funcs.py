
import os
from time import sleep


def get_queue_operation(queue):
        cls()
        print(f"Queue: {queue}\nChoose from one of the following operations to execute on the queue:")
        execute = input("""
            ADD - adds an element
            PEEK - preview the top most element in the queue
            REMOVE - removes the first element
            EXIT - exits program
        """).upper()
        if execute not in ["ADD", "PEEK", "REMOVE", "EXIT"]:
            print("\nInvalid command.")
            sleep(1.5)
            return
        return execute

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_queue_element(queue):
    available_letters = ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S']
    for letter in queue:
        try:
            available_letters.remove(letter)
        except ValueError:
            continue
    if not available_letters:
        print("Queue is full. Removing the head will make space to add a new one.")
        sleep(1.5)
        return
    print(f"Queue: {queue}")
    letters = f"[{', '.join(letter for letter in available_letters)}]"
    letter = input(f"\nChoose from one of the following letters to add to the queue: {letters}")
    if letter not in available_letters:
        print("\n\nInvalid selection made.")
        sleep(1.5)
        cls()
        return
    return letter
