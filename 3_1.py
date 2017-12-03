import math

def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

def turnLeft(direction):
    if direction == (1, 0):
        return (0,1)
    elif direction == (0, 1):
        return (-1,0)
    elif direction == (-1, 0):
        return (0,-1)
    else: # direction == (0, -1)
        return (1, 0)

def distance(position):
    return abs(position[0]) + abs(position[1])

def solve(input):
    """
    solves day 3 part 1 for given input > 0
    """
    assert input > 0, "input %d must be greater than 0" % input
    direction = (1, 0)
    position = (0, 0)
    step_size = 1
    number = 1
    while number <= input:
        for _ in range(0, step_size):
            position = move(position, direction)
            number += 1
            # print ("%d at (%d,%d)" % (number, position[0], position[1]))
            if number == input:
                return distance(position)
        if position[0] == position[1]:
            step_size += 1
        direction = turnLeft(direction)
    return 0

# print solve(0)

print solve(1)
print solve(12)
print solve(23)
print solve(1024)
print solve(368078)
