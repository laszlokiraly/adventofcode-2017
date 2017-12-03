"""
solution to day 3 part 2
"""

def move(position, direction):
    """
    return the new position after moving in given direction
    """
    return (position[0] + direction[0], position[1] + direction[1])

def turn_left(direction):
    """
    return the new direction after a left turn
    """
    if direction == (1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (-1, 0)
    elif direction == (-1, 0):
        return (0, -1)
    # else direction == (0, -1)
    return (1, 0)

def get_adjacents_value(grid_dict, position):
    """
    returns the sums of all adjacent position's values
    """
    value = 0
    for x_pos in range(-1, 2):
        for y_pos in range(-1, 2):
            if (x_pos != 0) or (y_pos != 0):
                adj_position = move(position, (x_pos, y_pos))
                adj = grid_dict.get(adj_position)
                value += adj if adj else 0
    return value

def solve(number):
    """
    solves day_pos 3 part 2 for given number > 0
    """
    assert number > 0, "number %d must be greater than 0" % number
    grid_dict = {}
    direction = (1, 0)
    position = (0, 0)
    step_size = 1
    number = 1
    value = 1
    grid_dict.update({position: value})
    while number <= number:
        for _ in range(0, step_size):
            position = move(position, direction)
            number += 1
            value = get_adjacents_value(grid_dict, position)
            grid_dict.update({position: value})
            if number == number:
                return value
        if position[0] == position[1]:
            step_size += 1
        direction = turn_left(direction)
    return value

# for number in range(1, 100):
#     print "%d: %d" % (number, solve(number))

print "%d: %d" % (65, solve(65))

# print "%d: %d" % (368078, solve(368078))
