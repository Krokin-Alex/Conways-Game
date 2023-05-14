import random


def print_hello_world():
    print("Hello, world!")


# Create an empty 2D array filled with None [ [], [], [] ]
def create_world(rows, columns):
    worldarray = [[None] * columns for _ in range(rows)]
    return worldarray


# Fill 2D array with random 0 and 1
def init_world(array):
    for row in range(len(array)):
        for column in range(len(array[row])):
            array[row][column] = random.randint(0, 1)


# Print to text console world array
def print_console_world(array):
    character = None
    for row in range(len(array)):
        for column in range(len(array[row])):
            if array[row][column] == 0:
                character = " "
            else:
                character = "*"
            print(character, sep="", end="")
        print()
