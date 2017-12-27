"""
solution for day 11 part 1 and 2
"""
import re
import util

DAY11_INPUT = util.load_input('day11.input')[0]

def solve(input_data):
    """
    solve day 11 part 1 and 2
    """
    x_coor = 0
    y_coor = 0
    max_distance = 0
    for direction in re.split(r'[,]+', input_data):
        if direction == 'n':
            y_coor += 1
        elif direction == 'ne':
            x_coor += 1
            y_coor += 1
        elif direction == 'se':
            x_coor += 1
        if direction == 's':
            y_coor -= 1
        elif direction == 'sw':
            x_coor -= 1
            y_coor -= 1
        elif direction == 'nw':
            x_coor -= 1
        max_distance = max(max_distance, distance(x_coor, y_coor))
    return distance(x_coor, y_coor), max_distance

def distance(x_coor, y_coor):
    """
    distance from (0,0) of a point in the hex coord system
    """
    if x_coor == y_coor:
        return x_coor
    elif abs(x_coor) > abs(y_coor):
        return abs(x_coor-y_coor) + abs(y_coor)
    return abs(y_coor-x_coor) + abs(x_coor)

print solve('ne,ne,ne')
print solve('ne,ne,sw,sw')
print solve('ne,ne,s,s')
print solve('se,sw,se,sw,sw')

print solve(DAY11_INPUT)
