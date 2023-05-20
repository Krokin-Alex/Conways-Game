from utilities import (
    create_world,
    init_world,
    print_console_world,
    print_console_world_debug,
    clear_screen,
    build_new_world,
    count_all_cells,
)
import time
import keyboard

rows = 25
cols = 80
world = []


def main():
    generation = 0

    world = create_world(rows, cols)
    init_world(world)
    clear_screen()
    print_console_world(world)

    while True:
        # Check for Ctrl-C or escape button press
        if keyboard.is_pressed("Ctrl+C") or keyboard.is_pressed("esc"):
            break

        generation += 1
        world = build_new_world(world, rows, cols)

        clear_screen()
        print_console_world(world)
        print(
            "Generaion:", generation, "Number or alive cells:", count_all_cells(world)
        )

        time.sleep(0.1)


if __name__ == "__main__":
    main()
