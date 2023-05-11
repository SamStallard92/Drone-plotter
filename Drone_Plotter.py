# define the size of the grid
GRID_SIZE = 12


def read_route_instructions(file_name):
    """
    Reads the route instructions from the given file and returns them as a list.
    Returns None if the file is not found.
    """
    try:
        with open(file_name, 'r') as f:
            route_instructions = [int(x) if i < 2 else x.upper() for i, x in enumerate(f.read().split())]
        return route_instructions
    except FileNotFoundError:
        return None


def plot_route(route_instructions):
    """
    Plots the given route instructions on a grid and returns the coordinates of the route.
    Returns None if the route is outside of the grid.
    """
    # initialize the grid
    grid = [[' ' for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

    # get the starting coordinates
    x, y = route_instructions[0], route_instructions[1]
    if x < 1 or x > GRID_SIZE or y < 1 or y > GRID_SIZE:
        return None

    # mark the starting point on the grid
    grid[y - 1][x - 1] = 'x'

    # plot the route
    coords = [(x, y)]
    for direction in route_instructions[2:]:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        if x < 1 or x > GRID_SIZE or y < 1 or y > GRID_SIZE:
            return None
        grid[y - 1][x - 1] = 'x'
        coords.append((x, y))

    # print the grid
    print('Grid Layout')
    print('   : ' + ':'.join([' ' for i in range(GRID_SIZE)]) + ':')
    print('---:' + ':'.join(['---' for i in range(GRID_SIZE)]) + ':')
    for i in range(GRID_SIZE):
        row = GRID_SIZE - i
        print(f'{row:2d}: ' + ':'.join(grid[i]) + ':')
        print('---:' + ':'.join(['---' for i in range(GRID_SIZE)]) + ':')

    # print the coordinates
    print('\nCoordinates')
    for coord in coords:
        print(f'({coord[0]}, {coord[1]})')
    return coords


# loop to get route instructions files from the user
while True:
    file_name = input('Enter the next route instructions file, or enter STOP to finish: ')
    if file_name.upper() == 'STOP':
        break
    route_instructions = read_route_instructions(file_name)
    if route_instructions is None:
        print('File not found')
        continue
    coords = plot_route(route_instructions)
    if coords is None:
        print('Error: The route is outside of the grid')
