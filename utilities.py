import os
import random


# Clear console screen
def clear_screen():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")


# Create an empty 2D array filled with None [ [], [], [] ]
def create_world(rows, columns):
    worldarray = [[0] * columns for _ in range(rows)]
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
            if array[row][column] == 1:
                character = "*"
            else:
                character = " "
            print(character, end="")
        print()


# Print debug to text console world array
def print_console_world_debug(array):
    for row in range(len(array)):
        for column in range(len(array[row])):
            print(array[row][column], "", end="")
        print()


# Count how many "alive" cells we have
def count_all_cells(array):
    count = 0
    for row in range(len(array)):
        for column in range(len(array[row])):
            count = count + array[row][column]
    return count


# Count neightbours for 3x3 cell
def count_neighbours(array, row, column):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            count = count + array[i][j]

    count = count - array[row][column]
    return count


# Create next generation world, main game logic
def build_new_world(array, rows, cols):
    new_world = create_world(rows, cols)
    count = 0

    for row in range(1, len(array) - 1):
        for column in range(1, len(array[row]) - 1):
            # считаем соседей
            count = count_neighbours(array, row, column)

            # world logic
            # if cell is alive
            if array[row][column] == 1:
                if count < 2 or count > 3:
                    new_world[row][column] = 0
                else:
                    new_world[row][column] = 1
            # if cell is dead
            else:
                if count == 3:
                    new_world[row][column] = 1
                else:
                    new_world[row][column] = 0

    return new_world
