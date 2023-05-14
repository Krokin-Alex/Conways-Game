from utilities import create_world, init_world, print_console_world

rows = 25
cols = 100
world1 = []
world2 = []


def main():
    world1 = create_world(rows, cols)
    init_world(world1)

    print_console_world(world1)


if __name__ == "__main__":
    main()
